import os
from experiments.sensitivity import run_sensitivity
from experiments.strategy_comparison import run_strategy_comparison
from experiments.runtime_scaling import run_runtime_scaling
from experiments.convergence_analysis import run_convergence
from experiments.certification_analysis import run_certification
from plots.plot_generator import (
    plot_heatmap,
    plot_runtime,
    plot_strategy_bar,
    plot_convergence,
    plot_certification_boundary
)


def main():

    os.makedirs("plots", exist_ok=True)
    os.makedirs("results", exist_ok=True)

    print("Running Sensitivity...")
    load_levels, reserve_levels, risk_matrix = run_sensitivity()
    plot_heatmap(load_levels, reserve_levels, risk_matrix)

    print("Running Strategy Comparison...")
    strategies, risks = run_strategy_comparison()
    plot_strategy_bar(strategies, risks)

    print("Running Runtime Scaling...")
    sizes, runtimes = run_runtime_scaling()
    plot_runtime(sizes, runtimes)

    print("Running Convergence Analysis...")
    Ns, conv_risks = run_convergence()
    plot_convergence(Ns, conv_risks)

    print("Running Certification Analysis...")
    alpha = 0.05
    reserves, cert_risks, certified = run_certification(alpha)
    plot_certification_boundary(reserves, cert_risks, certified, alpha)

    print("All plots and tables generated successfully.")


if __name__ == "__main__":
    main()