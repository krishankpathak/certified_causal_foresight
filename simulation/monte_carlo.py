from models.grid_model import GridModel
from simulation.scenario_engine import ScenarioEngine
from models.risk_estimator import RiskEstimator


class MonteCarloSimulator:

    def __init__(self, N=50, load_multiplier=1.0):
        self.N = N
        self.load_multiplier = load_multiplier

    def run(self, reserve_ratio):

        violations = 0

        for _ in range(self.N):

            grid = GridModel()
            engine = ScenarioEngine(
                grid,
                load_multiplier=self.load_multiplier,
                line_limit_factor=0.8  # tighten lines
            )

            if engine.simulate(reserve_ratio):
                violations += 1

        estimator = RiskEstimator()
        return estimator.estimate(violations, self.N)