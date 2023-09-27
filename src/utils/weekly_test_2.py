import random
import math


class LaplaceDistribution:
    def __init__(self, rand, loc, scale):
        self.rand = rand
        self.loc = loc
        self.scale = scale

    def pdf(self, x):
        if self.scale <= 0:
            raise ValueError("Skála paraméter csak pozitív lehet.")

        pdf = (1.0 / (2.0 * self.scale)) * math.exp(-abs(x - self.loc) / self.scale)
        return pdf