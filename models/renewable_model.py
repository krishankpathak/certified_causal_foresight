import numpy as np


class RenewableModel:

    def __init__(self, sigma_ratio=0.3):
        self.sigma_ratio = sigma_ratio

    def apply_uncertainty(self, net):

        for i in net.gen.index:

            base = net.gen.at[i, "p_mw"]
            noise = np.random.normal(0, self.sigma_ratio * base)
            net.gen.at[i, "p_mw"] = max(0, base + noise)