import math
import random

import pyerf
from scipy.special import gamma, gammainc, gammaincinv


class UniformDistribution:
    def __init__(self, rand, a, b):
        self.rand = rand
        self.a = a
        self.b = b

    def pdf(self, x):
        if self.a <= x <= self.b:
            pdf_num = 1 / (self.b - self.a)
        return pdf_num

    def cdf(self, x):
        if x < self.a:
            cdf_num = 0
        elif self.a <= x <= self.b:
            cdf_num = (x - self.a) / (self.b - self.a)
        elif self.b < x:
            cdf_num = 1
        return cdf_num

    def ppf(self, p):
        inv_num = math.sqrt((1/12 * (self.b - self.a) ** 2)) * math.sqrt(3) * (2 * p - 1) + 1/2 * (self.a + self.b)
        return inv_num

    def gen_rand(self):
        p = random.random()
        inv_num = math.sqrt((1/12 * (self.b - self.a) ** 2)) * math.sqrt(3) * (2 * p - 1) + 1/2 * (self.a + self.b)
        return inv_num

    def mean(self):
        mean_num = 1 / 2 * (self.a + self.b)
        return mean_num

    def median(self):
        med_num = 1 / 2 * (self.a + self.b)
        return med_num

    def variance(self):
        var_num = 1 / 12 * (self.b - self.a) ** 2
        return var_num

    def skewness(self):
        return 0

    def ex_kurtosis(self):
        kurt_num = -6 / 5
        return kurt_num

    def mvsk(self):
        moment_list = []
        mean_num = 1/2 * (self.a + self.b)
        kurt_num = -6/5
        mom2 = 1/12 * (self.b - self.a)
        mom3 = 0
        moment_list.append(mean_num)
        moment_list.append(mom2)
        moment_list.append(mom3)
        moment_list.append(kurt_num)
        return moment_list


class NormalDistribution:
    def __init__(self, rand, loc, scale):
        self.rand = rand
        self.loc = loc
        self.scale = scale

    def pdf(self, x):
        coefficient = 1 / (math.sqrt(self.scale) * math.sqrt(2 * math.pi))
        exponent = -0.5 * ((x - self.loc) / math.sqrt(self.scale)) ** 2
        pdf_num2 = coefficient * math.exp(exponent)
        return pdf_num2

    def cdf(self, x):
        erf_num = (x - self.loc)/(math.sqrt(self.scale) * math.sqrt(2))
        cdf_num2 = 1/2 * (1 + pyerf.erf(erf_num))
        return cdf_num2

    def ppf(self, p):
        inv_num2 = self.loc + math.sqrt(self.scale) * math.sqrt(2) * (1/pyerf.erf(2 * p -1))
        return inv_num2

    def gen_rand(self):
        u1 = random.uniform(0, 1)
        u2 = random.uniform(0, 1)
        z0 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
        return z0

    def mean(self):
        mean_num2 = self.loc
        return mean_num2

    def median(self):
        med_num2 = self.loc
        return med_num2

    def variance(self):
        var_num2 = self.scale
        return var_num2

    def skewness(self):
        return 0

    def ex_kurtosis(self):
        kurt_num2 = 0
        return kurt_num2

    def mvsk(self):
        moment_list = []
        mean_num2 = self.loc
        kurt_num2 = 0
        mom22 = self.scale
        mom32 = 0
        moment_list.append(mean_num2)
        moment_list.append(mom22)
        moment_list.append(mom32)
        moment_list.append(kurt_num2)

        return moment_list


class CauchyDistribution:
    def __init__(self, rand, loc, scale):
        self.rand = rand
        self.loc = loc
        self.scale = scale

    def cdf(self, x):
        cdf_num3 = 1/math.pi * math.atan((x - self.loc)/self.scale) + 1/2
        return cdf_num3

    def ppf(self, p):
        inv_num3 = self.loc + self.scale * math.tan(math.pi * (p - 1 / 2))
        return inv_num3

    def gen_rand(self):
        p = random.random()
        inv_num3 = self.loc + self.scale * math.tan(math.pi * (p - 1 / 2))
        return inv_num3

    def pdf(self, x):
        pdf_num3 = 1/(math.pi * self.scale * (1 + ((x - self.loc)/ self.scale) ** 2))
        return pdf_num3

    def mvsk(self):
        raise Exception("Moments undefined")


class LogisticDistribution:
    def __init__(self, rand, location, scale):
        self.rand = rand
        self.location = location
        self.scale = scale

    def pdf(self, x):
        pdf = (math.exp(-(x - self.location) / self.scale) /(self.scale * (1 + math.exp(-(x - self.location) / self.scale)) ** 2))
        return pdf

    def cdf(self, x):
        cdf = 1 / (1 + math.exp(-(x - self.location) / self.scale))
        return cdf

    def ppf(self, p):
        ppf_one = p / (1 - p)
        ppf = self.location + self.scale * math.log(ppf_one)
        return ppf

    def gen_rand(self):
        p_value = random.random()
        ppf_one = p_value / (1 - p_value)
        logistic_random = self.location + self.scale * math.log(ppf_one)
        return logistic_random

    def mean(self):
        mean = self.location
        return mean

    def variance(self):
        var = ((self.scale ** 2) * math.pi ** 2) / 3
        return var

    def skewness(self):
        skew = 0
        return skew

    def ex_kurtosis(self):
        kurt = 6 / 5
        return kurt

    def mvsk(self):
        return [self.mean(), self.variance(), self.skewness(), self.ex_kurtosis()]


class ChiSquaredDistribution:
    def __init__(self, rand, dof):
        self.rand = rand
        self.dof = dof

    def pdf(self, x):
        pdf = (1 / (2 ** (self.dof / 2) * gamma(self.dof / 2))) * x ** ((self.dof / 2) - 1) * math.exp(-x / 2)
        return pdf

    def cdf(self, x):
        cdf = gammainc((self.dof / 2), (x / 2))
        return cdf

    def ppf(self, p):
        ppf = gammaincinv(self.dof / 2, p) * 2
        return ppf

    def gen_rand(self):
        p = random.random()
        chi_random = gammaincinv(self.dof / 2, p) * 2
        return chi_random

    def mean(self):
        mean = self.dof
        return mean

    def variance(self):
        var = self.dof * 2
        return var

    def skewness(self):
        skew = math.sqrt((8 / self.dof))
        return skew

    def ex_kurtosis(self):
        kurt = 12 / self.dof
        return kurt

    def mvsk(self):
        return [self.mean(), self.variance(), self.skewness(), self.ex_kurtosis()]
