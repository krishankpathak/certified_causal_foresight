"""
baseline.py

Baseline comparison experiment.

Compares:
- Deterministic dispatch
- Conservative dispatch
- Aggressive dispatch

Evaluates:
- Estimated cascading risk
- Certification status
- False security condition
"""

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.append(project_root)

from simulation.monte_carlo import MonteCarloSimulator
from certification.certifier import DecisionCertifier


def run_baseline():

    print("\n============================================")
    print("BASELINE COMPARISON EXPERIMENT")
    print("============================================\n")

    # Monte Carlo simulator
    simulator = MonteCarloSimulator(N=500, T=6)

    # Certification layer
    certifier = DecisionCertifier(alpha=0.05, confidence=0.95, N=500, T=6)

    strategies = ["deterministic", "conservative", "aggressive"]

    baseline_results = []

    for strategy in strategies:

        # Raw Monte Carlo risk
        mc_result = simulator.run(dispatch_type=strategy)

        # Certified result
        cert_result = certifier.evaluate_dispatch(strategy)

        false_security = (
            mc_result["probability"] > certifier.alpha
            and cert_result["certified"] is True
        )

        baseline_results.append({
            "strategy": strategy,
            "risk": mc_result["probability"],
            "violations": mc_result["violations"],
            "certified": cert_result["certified"],
            "false_security": false_security
        })

    # -------------------------------------------------
    # Print structured output
    # -------------------------------------------------

    for r in baseline_results:

        print("Dispatch Strategy :", r["strategy"])
        print("Estimated Risk    :", r["risk"])
        print("Violations        :", r["violations"])
        print("Certified         :", r["certified"])
        print("False Security    :", r["false_security"])
        print("--------------------------------------------")

    return baseline_results


# -------------------------------------------------
# RUN
# -------------------------------------------------
if __name__ == "__main__":
    run_baseline()
