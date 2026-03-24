import time
import pandas as pd
from simulation.monte_carlo import MonteCarloSimulator


def run_runtime_scaling():

    sample_sizes = [20, 50, 100, 200]
    runtimes = []

    for N in sample_sizes:

        simulator = MonteCarloSimulator(N=N, load_multiplier=1.4)

        start = time.time()
        simulator.run(reserve_ratio=0.05)
        end = time.time()

        runtimes.append(end - start)

    df = pd.DataFrame({
        "Samples": sample_sizes,
        "Runtime_sec": runtimes
    })

    df.to_csv("results/runtime_table.csv", index=False)

    return sample_sizes, runtimes