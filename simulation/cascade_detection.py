"""
cascade_detection.py

Simple overload-based cascade detector
for pandapower DC simulations.
"""


class CascadeDetector:

    def __init__(self, overload_ratio=1.05):
        self.overload_ratio = overload_ratio

    def detect(self, net):

        # If no DC results exist, return False
        if not hasattr(net, "res_line"):
            return False

        overload = False

        for i in net.line.index:
            loading = net.res_line.at[i, "loading_percent"] / 100
            if loading > self.overload_ratio:
                overload = True
                break

        return overload