"""PPO wrapper for MultiDiscrete join-order / join-method / scan-method / index actions.

PPO (Proximal Policy Optimization) is chosen because:
1. It supports MultiDiscrete action spaces natively in Stable-Baselines3.
2. The 4D action (join order, join method, scan method, index) is naturally
   represented as independent categorical decisions.
3. On-policy learning is appropriate for our single-step MDP where each
   episode is one query optimization.
4. PPO's clipped objective prevents destructive policy updates, which is
   important when rewards are noisy (PostgreSQL timing variance).
"""

from __future__ import annotations

from pathlib import Path

from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv

from sql_optimizer.environment import SQLOptimizerEnv


def make_ppo(
    env: SQLOptimizerEnv,
    *,
    seed: int = 42,
    learning_rate: float = 3e-4,
    n_steps: int = 64,
    batch_size: int = 32,
    n_epochs: int = 10,
    ent_coef: float = 0.01,
    device: str = "cpu",
) -> PPO:
    vec = DummyVecEnv([lambda: env])
    return PPO(
        "MlpPolicy",
        vec,
        verbose=1,
        learning_rate=learning_rate,
        n_steps=n_steps,
        batch_size=batch_size,
        n_epochs=n_epochs,
        ent_coef=ent_coef,
        gamma=0.99,
        seed=seed,
        device=device,
    )


def save_model(model: PPO, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    model.save(str(path))


def load_model(path: Path, env: SQLOptimizerEnv) -> PPO:
    return PPO.load(str(path), env=DummyVecEnv([lambda: env]))
