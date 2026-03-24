import pandapower as pp
import numpy as np
import copy
from models.dispatch_model import DispatchModel
from models.renewable_model import RenewableModel
from simulation.cascade_detection import CascadeDetector


class ScenarioEngine:

    def __init__(self, grid_model,
                 load_multiplier=1.0,
                 line_limit_factor=0.8):

        self.base_net = grid_model.net
        self.load_multiplier = load_multiplier
        self.line_limit_factor = line_limit_factor

        self.detector = CascadeDetector()
        self.renewable = RenewableModel()

    def simulate(self, reserve_ratio):

        # ✅ Correct deep copy
        net = copy.deepcopy(self.base_net)

        # Apply load scaling safely
        net.load["p_mw"] = net.load["p_mw"] * self.load_multiplier

        # Tighten line limits
        net.line["max_loading_percent"] = 100 * self.line_limit_factor

        # Dispatch
        dispatch = DispatchModel(net)
        dispatch.dispatch(reserve_ratio)

        # Renewable uncertainty
        self.renewable.apply_uncertainty(net)

        # Random generator outage (5%)
        if np.random.rand() < 0.05:
            idx = np.random.choice(net.gen.index)
            net.gen.at[idx, "p_mw"] = 0

        # Run DC power flow
        pp.rundcpp(net)

        return self.detector.detect(net)