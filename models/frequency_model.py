"""
frequency_model.py

Improved frequency deviation model
with normalization and damping.
"""

class FrequencyModel:

    def __init__(self, H=5.0, nominal_freq=60.0, S_base=100.0, D=1.0):

        self.H = H
        self.nominal_freq = nominal_freq
        self.S_base = S_base
        self.D = D  # damping factor
        self.freq = nominal_freq

    def update(self, generation, load):

        imbalance = generation - load  # MW

        # Normalize by system base
        delta_f = imbalance / (2 * self.H * self.S_base)

        # Apply damping
        delta_f -= self.D * (self.freq - self.nominal_freq) * 0.01

        self.freq += delta_f

        return self.freq

    def reset(self):
        self.freq = self.nominal_freq

    def violation(self, threshold=0.5):
        return abs(self.freq - self.nominal_freq) > threshold
