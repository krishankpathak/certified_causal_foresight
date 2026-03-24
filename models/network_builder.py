import numpy as np


class NetworkBuilder:

    def __init__(self, data):

        self.buses = data["buses"]
        self.generators = data["generators"]
        self.loads = data["loads"]

        # Combine branches + transformers
        self.branches = data["branches"] + data["transformers"]

        self.bus_ids = sorted(self.buses.keys())
        self.bus_index = {bus: idx for idx, bus in enumerate(self.bus_ids)}

        # Slack bus detection (type == 3)
        self.slack_bus = None
        for bus_id, bus in self.buses.items():
            if bus["type"] == 3:
                self.slack_bus = bus_id
                break

        print("Total buses:", len(self.buses))
        print("Total raw branches:", len(self.branches))
        print("Slack bus:", self.slack_bus)

    # -------------------------------------------------
    def build_susceptance_matrix(self):

        n = len(self.bus_ids)
        B = np.zeros((n, n))

        valid = 0

        for branch in self.branches:

            if not isinstance(branch, list):
                continue

            try:
                i_bus = int(branch[0])
                j_bus = int(branch[1])
                x = float(branch[4])
                status = int(branch[9])
            except:
                continue

            if status == 0 or x == 0:
                continue

            if i_bus not in self.bus_index or j_bus not in self.bus_index:
                continue

            i = self.bus_index[i_bus]
            j = self.bus_index[j_bus]

            b = 1.0 / x

            B[i, j] -= b
            B[j, i] -= b
            B[i, i] += b
            B[j, j] += b

            valid += 1

        self.B = B

        print("Valid branches in B matrix:", valid)