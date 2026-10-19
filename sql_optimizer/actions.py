"""Discrete optimization actions: join order, join method, scan method, index.

The agent never outputs a numeric cost-reduction percentage. Actions only
select among concrete PostgreSQL knobs, SQL rewrites, and index candidates.

Action dimensions
─────────────────
  ┌── join_order_idx   : which candidate JOIN rewrite (0 = original)
  ├── join_method_idx  : default / hash / merge / nestloop
  ├── scan_method_idx  : default / seqscan / indexscan / bitmapscan
  └── index_idx        : 0 = no index, 1..k = candidate column

Every action maps to a real PostgreSQL intervention (GUC change, SQL
rewrite, or CREATE INDEX).  The effect is verified by EXPLAIN JSON.
"""

from __future__ import annotations

from dataclasses import dataclass

from sql_optimizer.database import (
    JOIN_METHOD_GUCS,
    JOIN_METHOD_NAMES,
    SCAN_METHOD_GUCS,
    SCAN_METHOD_NAMES,
)

# Caps keep the MultiDiscrete space fixed across queries.
MAX_JOIN_ORDERS = 8
MAX_INDEX_CANDIDATES = 6  # plus slot 0 = "no extra index"
N_JOIN_METHODS = len(JOIN_METHOD_NAMES)    # 4
N_SCAN_METHODS = len(SCAN_METHOD_NAMES)    # 4


@dataclass(frozen=True)
class OptimizationAction:
    """A concrete, discrete optimization decision.

    No field represents a percentage, cost reduction, or any value that
    would be used to artificially scale PostgreSQL costs.
    """

    join_order_idx: int
    join_method_idx: int
    scan_method_idx: int
    index_idx: int

    @property
    def join_method(self) -> str:
        idx = int(self.join_method_idx) % N_JOIN_METHODS
        return JOIN_METHOD_NAMES[idx]

    @property
    def scan_method(self) -> str:
        idx = int(self.scan_method_idx) % N_SCAN_METHODS
        return SCAN_METHOD_NAMES[idx]

    @property
    def join_gucs(self) -> dict[str, str]:
        return dict(JOIN_METHOD_GUCS[self.join_method])

    @property
    def scan_gucs(self) -> dict[str, str]:
        return dict(SCAN_METHOD_GUCS[self.scan_method])

    @property
    def all_gucs(self) -> dict[str, str]:
        """Combined GUCs for both join and scan method preferences."""
        gucs = self.join_gucs
        gucs.update(self.scan_gucs)
        return gucs

    def as_tuple(self) -> tuple[int, int, int, int]:
        return (
            int(self.join_order_idx),
            int(self.join_method_idx),
            int(self.scan_method_idx),
            int(self.index_idx),
        )


def decode_multi(action) -> OptimizationAction:
    """Decode Gymnasium MultiDiscrete action [order, method, scan, index]."""
    arr = list(action)
    return OptimizationAction(
        join_order_idx=int(arr[0]),
        join_method_idx=int(arr[1]),
        scan_method_idx=int(arr[2]),
        index_idx=int(arr[3]),
    )


def flatten_dims() -> int:
    """Total size of the flattened discrete action space."""
    return MAX_JOIN_ORDERS * N_JOIN_METHODS * N_SCAN_METHODS * (MAX_INDEX_CANDIDATES + 1)


def decode_flat(action_id: int) -> OptimizationAction:
    """Decode a single Discrete id used by DQN.

    The encoding order (least significant first):
      index → scan_method → join_method → join_order
    """
    n_idx = MAX_INDEX_CANDIDATES + 1
    n_scan = N_SCAN_METHODS
    n_method = N_JOIN_METHODS
    aid = int(action_id) % flatten_dims()
    index_idx = aid % n_idx
    aid //= n_idx
    scan_method_idx = aid % n_scan
    aid //= n_scan
    join_method_idx = aid % n_method
    join_order_idx = aid // n_method
    return OptimizationAction(join_order_idx, join_method_idx, scan_method_idx, index_idx)


def encode_flat(action: OptimizationAction) -> int:
    """Encode an action as a single Discrete id (inverse of decode_flat)."""
    n_idx = MAX_INDEX_CANDIDATES + 1
    n_scan = N_SCAN_METHODS
    return (
        int(action.join_order_idx) * N_JOIN_METHODS * n_scan * n_idx
        + int(action.join_method_idx) * n_scan * n_idx
        + int(action.scan_method_idx) * n_idx
        + int(action.index_idx)
    )
