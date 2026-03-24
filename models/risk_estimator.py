"""
risk_estimator.py

Monte Carlo risk estimator with CI.
"""

from math import sqrt
from scipy.stats import norm


class RiskEstimator:

    def __init__(self, confidence=0.95):
        self.z = norm.ppf(confidence)

    def estimate(self, violations, N):

        p_hat = violations / N

        margin = self.z * sqrt((p_hat * (1 - p_hat)) / N) if N > 0 else 0
        lower = max(0, p_hat - margin)
        upper = min(1, p_hat + margin)

        return {
            "probability": p_hat,
            "ci_lower": lower,
            "ci_upper": upper
        }