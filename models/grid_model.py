import pandapower.networks as pn
import pandapower as pp


class GridModel:

    def __init__(self):

        # Load IEEE 14 bus test case
        self.net = pn.case14()

    def reset(self):
        self.net = pn.case14()

    def run_dc(self):
        pp.rundcpp(self.net)
        return self.net