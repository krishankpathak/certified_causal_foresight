import pandas as pd
from simulation.monte_carlo import MonteCarloSimulator


def run_certification(alpha):

    reserves = [0.01, 0.03, 0.05, 0.1, 0.15]
    risks = []
    certified = []

    for r in reserves:

        simulator = MonteCarloSimulator(N=150, load_multiplier=1.5)
        result = simulator.run(reserve_ratio=r)

        risk = result["probability"]
        risks.append(risk)

        certified.append(risk <= alpha)

    df = pd.DataFrame({
        "Reserve": reserves,
        "Risk": risks,
        "Certified": certified
    })

    df.to_csv("results/certification_table.csv", index=False)

    return reserves, risks, certified