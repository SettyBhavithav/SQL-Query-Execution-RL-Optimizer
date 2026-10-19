"""Historical entry point now trains the PostgreSQL closed-loop optimizer.

The previous simulated `cost_reduction` / `predicted_cost = true_cost * ...`
environment has been removed. This file delegates to `sql_optimizer.train`.
"""

from sql_optimizer.train import main

if __name__ == "__main__":
    main()
