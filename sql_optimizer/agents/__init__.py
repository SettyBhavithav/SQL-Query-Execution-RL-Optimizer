"""Discrete-action agents for the PostgreSQL optimizer environment.

Supported algorithms
────────────────────
- **PPO** (Proximal Policy Optimization): On-policy, supports MultiDiscrete
  actions natively. Suitable for the 4D action space
  (join order × join method × scan method × index).

- **DQN** (Deep Q-Network): Off-policy Q-learning for the flattened Discrete
  encoding of the same 4D action. Provides exploration via ε-greedy.

Why not SAC / DDPG?
───────────────────
SAC and DDPG require a *continuous* action space. The historical
``cost_reduction`` continuous action has been completely removed—all
optimization actions are now discrete PostgreSQL interventions. There
is no continuous parameter for these algorithms to optimize.
"""
