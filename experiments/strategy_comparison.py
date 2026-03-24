import pandas as pd
from simulation.monte_carlo import MonteCarloSimulator


def run_strategy_comparison():

    strategies = {
        "Low Reserve": 0.02,
        "Medium Reserve": 0.08,
        "High Reserve": 0.15
    }

    risks = []

    for name, reserve in strategies.items():

        simulator = MonteCarloSimulator(N=100, load_multiplier=1.4)
        result = simulator.run(reserve_ratio=reserve)

        risks.append(result["probability"])

    df = pd.DataFrame({
        "Strategy": list(strategies.keys()),
        "Risk": risks
    })

    df.to_csv("results/strategy_table.csv", index=False)

    return list(strategies.keys()), risks