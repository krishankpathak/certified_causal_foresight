class DispatchModel:

    def __init__(self, net):
        self.net = net

    def dispatch(self, reserve_ratio=0.1):

        total_load = self.net.load["p_mw"].sum()

        required_gen = total_load / (1 - reserve_ratio)

        gen_pmax = self.net.gen["max_p_mw"].values
        total_pmax = gen_pmax.sum()

        for i in range(len(self.net.gen)):

            share = gen_pmax[i] / total_pmax
            pg = share * required_gen
            pg = min(pg, gen_pmax[i])

            self.net.gen.at[i, "p_mw"] = pg