"""DQN wrapper over a flattened Discrete encoding of the 4D action space.

DQN (Deep Q-Network) is chosen because:
1. It provides off-policy Q-learning, allowing the replay buffer to reuse
   past PostgreSQL execution results.
2. The MultiDiscrete 4D action (join order, join method, scan method, index)
   is flattened to a single integer for DQN's Discrete space.
3. ε-greedy exploration naturally explores different optimization strategies.
4. DQN is a strong baseline for discrete action problems.

Trade-off vs PPO: DQN has a larger action space (flattened) which may be
slower to learn, but benefits from replay buffer efficiency.
"""

from __future__ import annotations

from pathlib import Path

from stable_baselines3 import DQN
from stable_baselines3.common.vec_env import DummyVecEnv

from sql_optimizer.environment import SQLOptimizerEnv


def make_dqn(
    env: SQLOptimizerEnv,
    *,
    seed: int = 42,
    learning_rate: float = 1e-4,
    buffer_size: int = 10_000,
    batch_size: int = 32,
    exploration_fraction: float = 0.3,
    exploration_final_eps: float = 0.05,
    device: str = "cpu",
) -> DQN:
    if not env.discrete_flat:
        raise ValueError("DQN requires SQLOptimizerEnv(discrete_flat=True)")
    vec = DummyVecEnv([lambda: env])
    return DQN(
        "MlpPolicy",
        vec,
        verbose=1,
        learning_rate=learning_rate,
        buffer_size=buffer_size,
        batch_size=batch_size,
        gamma=0.99,
        exploration_fraction=exploration_fraction,
        exploration_final_eps=exploration_final_eps,
        seed=seed,
        device=device,
    )


def save_model(model: DQN, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    model.save(str(path))


def load_model(path: Path, env: SQLOptimizerEnv) -> DQN:
    return DQN.load(str(path), env=DummyVecEnv([lambda: env]))
