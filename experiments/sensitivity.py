import numpy as np
import pandas as pd
from simulation.monte_carlo import MonteCarloSimulator


def run_sensitivity():

    # Reduced grid for stable runtime
    load_levels = np.linspace(1.0, 1.6, 4)
    reserve_levels = np.linspace(0.02, 0.15, 4)

    risk_matrix = np.zeros((len(load_levels), len(reserve_levels)))

    for i, lm in enumerate(load_levels):
        for j, rr in enumerate(reserve_levels):

            print(f"Load {lm:.2f} | Reserve {rr:.2f}")

            simulator = MonteCarloSimulator(
                N=40,
                load_multiplier=lm
            )

            result = simulator.run(reserve_ratio=rr)

            risk_matrix[i, j] = result["probability"]

    # Save table
    df = pd.DataFrame(
        risk_matrix,
        index=[f"{lm:.2f}" for lm in load_levels],
        columns=[f"{rr:.2f}" for rr in reserve_levels]
    )

    df.to_csv("results/risk_surface_table.csv")

    return load_levels, reserve_levels, risk_matrix