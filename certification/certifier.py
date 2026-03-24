"""
certifier.py

Statistical certification module
for Certified Causal Foresight framework.

Implements upper confidence bound (UCB)
based probabilistic certification.
"""

import os
import sys
from math import sqrt
from scipy.stats import norm

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.append(project_root)

from simulation.monte_carlo import MonteCarloSimulator


class DecisionCertifier:

    def __init__(self, alpha=0.05, confidence=0.95, N=500, T=6):

        self.alpha = alpha
        self.confidence = confidence
        self.z = norm.ppf(confidence)
        self.simulator = MonteCarloSimulator(N=N, T=T)

    # -------------------------------------------------
    def evaluate_dispatch(self, dispatch_type):

        result = self.simulator.run(dispatch_type=dispatch_type)

        p_hat = result["probability"]
        N = result["scenarios"]

        # Upper Confidence Bound
        margin = self.z * sqrt((p_hat * (1 - p_hat)) / N)
        upper_bound = p_hat + margin

        certified = upper_bound <= self.alpha

        return {
            "dispatch": dispatch_type,
            "estimated_risk": p_hat,
            "upper_confidence_bound": round(upper_bound, 4),
            "alpha_threshold": self.alpha,
            "certified": certified,
            "violations": result["violations"],
            "scenarios": N
        }

    # -------------------------------------------------
    def certify_all(self):

        strategies = [
            "deterministic",
            "conservative",
            "aggressive"
        ]

        results = []

        for strategy in strategies:
            results.append(self.evaluate_dispatch(strategy))

        return results


# -------------------------------------------------
# TEST BLOCK
# -------------------------------------------------
if __name__ == "__main__":

    certifier = DecisionCertifier(
        alpha=0.05,
        confidence=0.95,
        N=500,
        T=6
    )

    results = certifier.certify_all()

    print("\n====================================================")
    print("STATISTICAL DECISION CERTIFICATION REPORT")
    print("Risk Threshold (alpha):", certifier.alpha)
    print("Confidence Level:", certifier.confidence)
    print("====================================================\n")

    for r in results:

        print("Dispatch Strategy         :", r["dispatch"])
        print("Scenarios Evaluated       :", r["scenarios"])
        print("Observed Violations       :", r["violations"])
        print("Estimated Risk (p̂)        :", r["estimated_risk"])
        print("Upper Confidence Bound    :", r["upper_confidence_bound"])
        print("Certified (UCB ≤ α)       :", r["certified"])
        print("----------------------------------------------------")
