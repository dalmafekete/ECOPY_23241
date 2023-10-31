import pandas as pd
import statsmodels.api as sm
import numpy as np

class LinearRegressionSM:
    def __init__(self, left_hand_side, right_hand_side):
        self.left_hand_side = left_hand_side
        self.right_hand_side = right_hand_side
        self.model = None

    def fit(self):
        X = sm.add_constant(self.right_hand_side)
        y = self.left_hand_side
        model = sm.OLS(y, X).fit()
        self.model = model
        print(model.summary())

    def get_params(self):
        beta_coefficients = self.model.params
        beta_coefficients.name = 'Beta coefficients'
        return beta_coefficients

    def get_pvalues(self):
        p_values = self.model.pvalues
        p_values.name = 'P-values for the corresponding coefficients'
        return p_values

    def get_wald_test_result(self, restriction_matrix):
        wald_test = self.model.wald_test(restriction_matrix, scalar = True)
        fvalue = wald_test.statistic
        pvalue = wald_test.pvalue
        return f"F-value: {fvalue:.2f}, p-value: {pvalue:.3f}"

    def get_model_goodness_values(self):
        ars = self.model.rsquared_adj
        ak = self.model.aic
        by = self.model.bic
        return f"Adjusted R-squared: {ars:.3f}, Akaike IC: {ak:.2e}, Bayes IC: {by:.2e}"

