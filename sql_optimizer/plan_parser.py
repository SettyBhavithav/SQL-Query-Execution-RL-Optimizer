"""Parse PostgreSQL EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) output.

Every measured metric used by the RL reward and state encoding is extracted
here from the real PostgreSQL JSON plan—never fabricated or scaled.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class PlanMetrics:
    """Measured metrics from a single EXPLAIN ANALYZE run.

    Every field is populated exclusively from the PostgreSQL JSON output.
    No field is ever computed as ``original_cost * (1 - reduction)`` or any
    equivalent artificial formula.
    """

    planning_time_ms: float = 0.0
    execution_time_ms: float = 0.0
    total_cost: float = 0.0
    startup_cost: float = 0.0
    actual_rows: float = 0.0
    plan_rows: float = 0.0
    shared_hit_blocks: int = 0
    shared_read_blocks: int = 0
    shared_written_blocks: int = 0
    temp_read_blocks: int = 0
    temp_written_blocks: int = 0
    peak_memory_kb: float = 0.0  # from Hash / Sort nodes when available
    join_operators: list[str] = field(default_factory=list)
    scan_operators: list[str] = field(default_factory=list)
    all_operators: list[str] = field(default_factory=list)
    node_count: int = 0
    max_actual_loops: int = 1
    signature: str = ""
    raw_plan: dict[str, Any] = field(default_factory=dict)

    @property
    def shared_blocks(self) -> int:
        return self.shared_hit_blocks + self.shared_read_blocks

    @property
    def total_blocks(self) -> int:
        return (
            self.shared_hit_blocks
            + self.shared_read_blocks
            + self.temp_read_blocks
            + self.temp_written_blocks
        )

    @property
    def cache_hit_ratio(self) -> float:
        total = self.shared_hit_blocks + self.shared_read_blocks
        if total == 0:
            return 1.0
        return self.shared_hit_blocks / total


JOIN_NODE_TYPES = {
    "Nested Loop",
    "Hash Join",
    "Merge Join",
    "Nested Loop Semi Join",
    "Hash Semi Join",
    "Merge Semi Join",
    "Nested Loop Anti Join",
    "Hash Anti Join",
    "Merge Anti Join",
}

SCAN_NODE_TYPES = {
    "Seq Scan",
    "Index Scan",
    "Index Only Scan",
    "Bitmap Heap Scan",
    "Bitmap Index Scan",
    "Tid Scan",
    "Subquery Scan",
    "Function Scan",
    "Values Scan",
    "CTE Scan",
    "Foreign Scan",
    "Custom Scan",
}


def parse_explain_json(payload: Any) -> PlanMetrics:
    """Extract measured metrics from EXPLAIN JSON (list or dict).

    This is the *only* function that translates raw PostgreSQL output into
    the metrics consumed by the RL reward.  It reads real numbers from the
    database engine; nothing is fabricated.
    """
    if isinstance(payload, list):
        root = payload[0] if payload else {}
    else:
        root = payload or {}

    plan = root.get("Plan") or {}
    metrics = PlanMetrics(
        planning_time_ms=float(root.get("Planning Time") or 0.0),
        execution_time_ms=float(root.get("Execution Time") or 0.0),
        total_cost=float(plan.get("Total Cost") or 0.0),
        startup_cost=float(plan.get("Startup Cost") or 0.0),
        actual_rows=float(plan.get("Actual Rows") or 0.0),
        plan_rows=float(plan.get("Plan Rows") or 0.0),
        raw_plan=root,
    )
    hits, reads = _root_or_sum_buffers(plan)
    metrics.shared_hit_blocks = hits
    metrics.shared_read_blocks = reads
    # Extract additional buffer counters from root node
    metrics.shared_written_blocks = int(plan.get("Shared Written Blocks") or 0)
    metrics.temp_read_blocks = int(plan.get("Temp Read Blocks") or 0)
    metrics.temp_written_blocks = int(plan.get("Temp Written Blocks") or 0)
    _walk(plan, metrics)
    metrics.signature = format_plan_tree(plan)
    return metrics


def _root_or_sum_buffers(plan: dict[str, Any]) -> tuple[int, int]:
    # PostgreSQL JSON usually reports buffer counters inclusive of children
    # on each node. Prefer the root totals; fall back to a tree sum when
    # only child nodes carry buffer fields (exclusive-style output).
    hits = int(plan.get("Shared Hit Blocks") or 0)
    reads = int(plan.get("Shared Read Blocks") or 0)
    if hits or reads:
        return hits, reads
    return _sum_buffers(plan)


def _sum_buffers(node: dict[str, Any]) -> tuple[int, int]:
    hits = int(node.get("Shared Hit Blocks") or 0)
    reads = int(node.get("Shared Read Blocks") or 0)
    for child in node.get("Plans") or []:
        c_hits, c_reads = _sum_buffers(child)
        hits += c_hits
        reads += c_reads
    return hits, reads


def _walk(node: dict[str, Any], metrics: PlanMetrics) -> None:
    ntype = str(node.get("Node Type") or "Unknown")
    metrics.all_operators.append(ntype)
    metrics.node_count += 1
    if ntype in JOIN_NODE_TYPES or "Join" in ntype:
        metrics.join_operators.append(ntype)
    if ntype in SCAN_NODE_TYPES or ntype.endswith("Scan"):
        metrics.scan_operators.append(ntype)
    # Track peak memory from Hash and Sort nodes
    peak = float(node.get("Peak Memory Usage") or 0)
    if peak > metrics.peak_memory_kb:
        metrics.peak_memory_kb = peak
    # Track maximum actual loops (indicates nested-loop explosion)
    loops = int(node.get("Actual Loops") or 1)
    if loops > metrics.max_actual_loops:
        metrics.max_actual_loops = loops
    for child in node.get("Plans") or []:
        _walk(child, metrics)


def format_plan_tree(node: dict[str, Any], indent: int = 0) -> str:
    """Human-readable operator tree used to detect unchanged plans.

    If the signature of baseline == optimized, the environment reports
    'plan unchanged' rather than claiming an optimization.
    """
    ntype = str(node.get("Node Type") or "Unknown")
    rel = node.get("Relation Name")
    alias = node.get("Alias")
    idx = node.get("Index Name")
    parts = [ntype]
    if rel:
        parts.append(rel)
    if alias and alias != rel:
        parts.append(f"({alias})")
    if idx:
        parts.append(f"using {idx}")
    label = " ".join(parts)
    lines = [("  " * indent) + label]
    for child in node.get("Plans") or []:
        lines.append(format_plan_tree(child, indent + 1))
    return "\n".join(lines)


def operator_fractions(operators: list[str], names: list[str]) -> list[float]:
    if not operators:
        return [0.0] * len(names)
    total = len(operators)
    return [operators.count(name) / total for name in names]


def plan_summary(metrics: PlanMetrics) -> dict[str, Any]:
    """Produce a human-readable summary dict for logging/reporting."""
    return {
        "exec_ms": round(metrics.execution_time_ms, 3),
        "planning_ms": round(metrics.planning_time_ms, 3),
        "cost": round(metrics.total_cost, 2),
        "actual_rows": metrics.actual_rows,
        "shared_hit": metrics.shared_hit_blocks,
        "shared_read": metrics.shared_read_blocks,
        "cache_hit_ratio": round(metrics.cache_hit_ratio, 4),
        "joins": metrics.join_operators,
        "scans": metrics.scan_operators,
        "node_count": metrics.node_count,
        "max_loops": metrics.max_actual_loops,
    }
