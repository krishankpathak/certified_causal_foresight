"""
raw_parser.py

Minimal IEEE RAW parser for:
- buses
- loads
- generators
- branches
- transformers

Designed specifically for IEEE 14-bus RAW file.
"""

import os


class RawParser:

    def __init__(self, filepath):
        self.filepath = filepath

        self.data = {
            "buses": {},
            "loads": {},
            "generators": {},
            "branches": [],
            "transformers": []
        }

    # -------------------------------------------------
    def parse(self):

        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"RAW file not found: {self.filepath}")

        with open(self.filepath, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()

        section = None

        for line in lines:

            line = line.strip()

            if line == "":
                continue

            # Section detection
            if "BUS DATA" in line:
                section = "bus"
                continue
            elif "LOAD DATA" in line:
                section = "load"
                continue
            elif "GENERATOR DATA" in line:
                section = "gen"
                continue
            elif "BRANCH DATA" in line:
                section = "branch"
                continue
            elif "TRANSFORMER DATA" in line:
                section = "xfmr"
                continue
            elif line.startswith("0 / END OF"):
                section = None
                continue

            # -------------------------------------------------
            # BUS
            if section == "bus":
                parts = line.split(",")
                try:
                    bus_id = int(parts[0])
                    bus_type = int(parts[3])
                except:
                    continue

                self.data["buses"][bus_id] = {
                    "type": bus_type
                }

            # -------------------------------------------------
            # LOAD
            elif section == "load":
                parts = line.split(",")
                try:
                    bus_id = int(parts[0])
                    pl = float(parts[5])
                except:
                    continue

                self.data["loads"][bus_id] = {
                    "pl": pl
                }

            # -------------------------------------------------
            # GENERATOR
            elif section == "gen":
                parts = line.split(",")
                try:
                    bus_id = int(parts[0])
                    pmax = float(parts[8])
                except:
                    continue

                self.data["generators"][(bus_id, 1)] = {
                    "pmax": pmax
                }

            # -------------------------------------------------
            # BRANCH
            elif section == "branch":
                parts = line.split(",")
                try:
                    i = int(parts[0])
                    j = int(parts[1])
                    x = float(parts[3])
                    rateA = float(parts[5])
                    status = int(parts[10])
                except:
                    continue

                self.data["branches"].append([
                    i, j, 0, 0, x, 0, rateA, 0, 0, status
                ])

            # -------------------------------------------------
            # TRANSFORMER (treat same as branch)
            elif section == "xfmr":
                parts = line.split(",")
                try:
                    i = int(parts[0])
                    j = int(parts[1])
                    x = float(parts[4])
                    rateA = float(parts[6])
                    status = int(parts[11])
                except:
                    continue

                self.data["transformers"].append([
                    i, j, 0, 0, x, 0, rateA, 0, 0, status
                ])

        print("Buses:", len(self.data["buses"]))
        print("Loads:", len(self.data["loads"]))
        print("Generators:", len(self.data["generators"]))
        print("Branches:", len(self.data["branches"]))
        print("Transformers:", len(self.data["transformers"]))

        return self.data


# -------------------------------------------------
if __name__ == "__main__":

    filepath = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "data",
        "raw",
        "IEEE 14 bus.raw"
    )

    parser = RawParser(filepath)
    parser.parse()