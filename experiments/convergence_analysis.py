import pandas as pd
from simulation.monte_carlo import MonteCarloSimulator


def run_convergence():

    Ns = [10, 20, 50, 100, 200]
    risks = []

    for N in Ns:

        simulator = MonteCarloSimulator(N=N, load_multiplier=1.4)
        result = simulator.run(reserve_ratio=0.05)

        risks.append(result["probability"])

    df = pd.DataFrame({
        "Samples": Ns,
        "Risk": risks
    })

    df.to_csv("results/convergence_table.csv", index=False)

    return Ns, risks