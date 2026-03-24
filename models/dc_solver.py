import numpy as np


class DCSolver:

    def __init__(self, builder):
        self.builder = builder
        self.B = builder.B
        self.bus_index = builder.bus_index
        self.slack_bus = builder.slack_bus

    # -------------------------------------------------
    def build_injection_vector(self, gen_dispatch, loads):

        n = len(self.bus_index)
        P = np.zeros(n)

        for (bus_id, _), pg in gen_dispatch.items():
            if bus_id in self.bus_index:
                P[self.bus_index[bus_id]] += pg

        for bus_id, load in loads.items():
            if bus_id in self.bus_index:
                P[self.bus_index[bus_id]] -= load["pl"]

        return P

    # -------------------------------------------------
    def solve(self, P):

        slack_idx = self.bus_index[self.slack_bus]

        B_red = np.delete(self.B, slack_idx, axis=0)
        B_red = np.delete(B_red, slack_idx, axis=1)
        P_red = np.delete(P, slack_idx)

        theta_red = np.linalg.solve(B_red, P_red)

        theta = np.zeros(len(P))
        idxs = list(range(len(P)))
        idxs.pop(slack_idx)

        for k, idx in enumerate(idxs):
            theta[idx] = theta_red[k]

        return theta

    # -------------------------------------------------
    def compute_line_flows(self, theta):

        flows = []

        for branch in self.builder.branches:

            if not isinstance(branch, list):
                continue

            try:
                i_bus = int(branch[0])
                j_bus = int(branch[1])
                x = float(branch[4])
                rateA = float(branch[6])
                status = int(branch[9])
            except:
                continue

            if status == 0 or x == 0:
                continue

            if i_bus not in self.bus_index or j_bus not in self.bus_index:
                continue

            i = self.bus_index[i_bus]
            j = self.bus_index[j_bus]

            flow = (theta[i] - theta[j]) / x

            flows.append({
                "flow": flow,
                "limit": rateA
            })

        if flows:
            max_flow = max(abs(f["flow"]) for f in flows)
            max_limit = max(f["limit"] for f in flows)

            print("Max Flow:", round(max_flow, 3))
            print("Max Limit:", round(max_limit, 3))

        return flows