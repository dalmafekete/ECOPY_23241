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

    def cdf(self, x):
        if self.scale <= 0:
            raise ValueError("Skála paraméter (b) csak pozitív lehet.")

        if x < self.loc:
            cdf = (1.0 / 2.0) * math.exp((x - self.loc) / self.scale)
        else:
            cdf = 1.0 - (1.0 / 2.0) * math.exp(-(x - self.loc) / self.scale)

        return cdf

    def mean(self):
        mean_num2 = self.loc
        return mean_num2

    def median(self):
        med_num2 = self.loc
        return med_num2

    def variance(self):
        var_num2 = 2 * (self.scale ** 2)
        return var_num2

    def skewness(self):
        return 0

    def ex_kurtosis(self):
        kurt_num2 = 3
        return kurt_num2

    def mvsk(self):
        moment_list = []
        mean_num2 = self.loc
        kurt_num2 = 3
        mom22 = 2 * (self.scale ** 2)
        mom32 = 0
        moment_list.append(mean_num2)
        moment_list.append(mom22)
        moment_list.append(mom32)
        moment_list.append(kurt_num2)

        return moment_list

    def gen_rand(self):
        e1 = -self.scale * math.log(random.random())
        e2 = -self.scale * math.log(random.random())
        return e1 -e2


class ParetoDistribution:
    def __init__(self, rand, scale, shape):
        self.rand = rand
        self.shape = shape
        self.scale = scale

    def pdf(self, x):
        pdf_num_one = self.shape * self.scale ** self.shape
        pdf_num_two = x ** (self.shape + 1)
        pdf2 = pdf_num_one / pdf_num_two

        return pdf2

    def cdf(self, x):
        cdf_one = (self.scale / x) ** self.shape
        cdf2 = 1 - cdf_one

        return cdf2

    def ppf(self, p):
        ppf_one = -1 / self.shape
        ppf2 = self.scale * (1 - p) ** ppf_one
        return ppf2

    def gen_random(self):
        u = random.random()
        x = self.scale / (u ** (1/self.shape))
        return x

    def mean(self):
        if self.shape <= 1:
            mean = float("infinite")
        else:
            mean = (self.shape * self.scale) / (self.shape - 1)
        return mean

    def median(self):
        median = x_min * (2 ** (1 / k) - 1)
        return median

    def variance(self):
        var1 = self.scale ** 2 * self.shape
        var2 = (self.shape - 1) ** 2 * (self.shape - 2)
        var = var1 / var2
        return var

    def skewness(self):
        one = (self.shape - 2) / self.shape
        two = (2 * (1 + self.shape)) / (self.shape - 3)
        skew = two * math.sqrt(one)
        return skew

    def ex_kurtosis(self):
        kurt_one = (6 * (self.shape ** 3 + self.shape ** 2 - 6 * self.shape - 2))
        kurt_two = self.shape * (self.shape - 3) * (self.shape - 4)
        kurt = kurt_one / kurt_two
        return kurt

    def mvsk(self):
        moment_list = []
        mean_num2 = (self.shape * self.scale) / (self.shape - 1)
        kurt_one = (6 * (self.shape ** 3 + self.shape ** 2 - 6 * self.shape - 2))
        kurt_two = self.shape * (self.shape - 3) * (self.shape - 4)
        kurt = kurt_one / kurt_two
        var1 = self.scale ** 2 * self.shape
        var2 = (self.shape - 1) ** 2 * (self.shape - 2)
        var = var1 / var2
        one = (self.shape - 2) / self.shape
        two = (2 * (1 + self.shape)) / (self.shape - 3)
        skew = two * math.sqrt(one)
        moment_list.append(mean_num2)
        moment_list.append(var)
        moment_list.append(skew)
        moment_list.append(kurt)

        return moment_list