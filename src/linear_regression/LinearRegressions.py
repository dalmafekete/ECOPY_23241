import pandas as pd
import statsmodels.api as sm
import numpy as np
from scipy.stats import t
from scipy.stats import f
import math

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

class LinearRegressionNP:
    def __init__(self, left_hand_side, right_hand_side):
        self.left_hand_side = left_hand_side
        self.right_hand_side = right_hand_side
        self.model = None

    def fit(self):
        X = self.right_hand_side
        y = self.left_hand_side
        X = np.column_stack((np.ones(X.shape[0]), X))
        XTX = np.dot(X.T, X)
        XTy = np.dot(X.T, y)
        beta = np.linalg.solve(XTX, XTy)
        alpha = beta[0]
        beta = beta[1:]
        return alpha, beta

    def get_params(self):
        X = self.right_hand_side
        y = self.left_hand_side
        X = np.column_stack((np.ones(X.shape[0]), X))

        XTX = np.dot(X.T, X)
        XTy = np.dot(X.T, y)

        beta = np.linalg.solve(XTX, XTy)

        beta_series = pd.Series(beta[0:], name="Beta coefficients")

        return beta_series

    def get_pvalues(self):
        X = self.right_hand_side
        y = self.left_hand_side
        X = np.column_stack((np.ones(X.shape[0]), X))

        XTX = np.dot(X.T, X)
        XTy = np.dot(X.T, y)

        beta = np.linalg.solve(XTX, XTy)

        y_pred = np.dot(X, beta)
        residuals = y - y_pred
        mse = np.sum(residuals ** 2) / (X.shape[0] - X.shape[1])

        t_stats = beta / np.sqrt(np.diagonal(mse * np.linalg.inv(XTX)))
        p_values = 2 * (1 - t.cdf(np.abs(t_stats), X.shape[0] - X.shape[1]))

        p_values_series = pd.Series(p_values[0:], name="P-values for the corresponding coefficients")

        return p_values_series

    def get_model_goodness_values(self):
        X = self.right_hand_side
        y = self.left_hand_side
        n = X.shape[0]
        p = X.shape[1]

        X = np.column_stack((np.ones(n), X))

        # Az OLS becsléshez szükséges mátrixok kiszámítása
        XTX = np.dot(X.T, X)
        XTy = np.dot(X.T, y)

        # A modell hibakvadrátumának számítása
        residuals = y - np.dot(X, self.get_params())
        sse = np.sum(residuals ** 2)

        # A teljes variabilitás számítása
        sst = np.sum((y - np.mean(y)) ** 2)

        # Centrált R-négyzet számítása
        crs = 1 - sse / sst

        # Módosított R-négyzet számítása
        ars = 1 - (sse / (n - p - 1)) / (sst / (n - 1))

        # Visszaadjuk az eredményt a megadott formátumban
        result_string = f"Centered R-squared: {crs:.3f}, Adjusted R-squared: {ars:.3f}"

        return result_string

    def get_wald_test_result(self, restriction_matrix):
        X = self.right_hand_side
        y = self.left_hand_side
        X = np.concatenate((np.ones((X.shape[0], 1)), self.right_hand_side), axis=1)
        R = np.asmatrix(restriction_matrix)

        XTX = np.dot(X.T, X)
        XTy = np.dot(X.T, y)
        beta_hat = np.linalg.solve(XTX, XTy)

        n = X.shape[0]
        df2 = n - X.shape[1]
        residuals = y - np.dot(X, beta_hat)
        sse = np.dot(residuals.T, residuals)/df2

        RBr = R @ beta_hat
        df1 = R.shape[0]
        wald_one = R @ np.linalg.inv(X.T @ X) @ R.T
        wald_test = RBr @ np.linalg.inv(wald_one) @ RBr.T/ df1/ sse

        p_value = 1 - f.cdf(wald_test.item(), df1, df2)
        result_string = f"Wald: {wald_test.item():.3f}, p-value: {p_value:.3f}"
        return result_string


class LinearRegressionGLS:
    def __init__(self, left_hand_side, right_hand_side):
        self.left_hand_side = left_hand_side
        self.right_hand_side = right_hand_side
        self.model = None
        self.beta_gls = None

    def fit(self):
        X = self.right_hand_side
        y = self.left_hand_side
        X = np.column_stack((np.ones(X.shape[0]), X))
        # OLS becslés
        XTX_inv = np.linalg.inv(X.T @ X)
        beta_ols = XTX_inv @ X.T @ y

        # Hibatagok kiszámítása
        residuals = y - X @ beta_ols

        # Hibatagok négyzetének kiszámítása
        squared_residuals = residuals ** 2

        # Új modell becslése

        new_beta_ols = XTX_inv @ X.T @ np.log(squared_residuals)

        # Becsült értékek kiszámítása
        y_hat = X @ new_beta_ols

        y_hat_exp = np.exp(y_hat)

        # V inverz mátrix készítése
        V_inv = np.diag(1 / np.sqrt(y_hat_exp))

        # GLS regresszió becslése
        self.beta_gls = np.linalg.inv(X.T @ V_inv @ X) @ X.T @ V_inv @ y

        return self.beta_gls

    def get_params(self):
        X = self.right_hand_side
        y = self.left_hand_side
        X = np.column_stack((np.ones(X.shape[0]), X))
        # OLS becslés
        XTX_inv = np.linalg.inv(X.T @ X)
        beta_ols = XTX_inv @ X.T @ y

        # Hibatagok kiszámítása
        residuals = y - X @ beta_ols

        # Hibatagok négyzetének kiszámítása
        squared_residuals = residuals ** 2

        # Új modell becslése

        new_beta_ols = XTX_inv @ X.T @ np.log(squared_residuals)

        # Becsült értékek kiszámítása
        y_hat = X @ new_beta_ols

        y_hat_exp = np.exp(y_hat)

        # V inverz mátrix készítése
        self.V_inv = np.diag(1 / np.sqrt(y_hat_exp))

        # GLS regresszió becslése
        beta_gls = np.linalg.inv(X.T @ self.V_inv @ X) @ X.T @ self.V_inv @ y

        beta_series = pd.Series(beta_gls[0:4], name="Beta coefficients")
        return beta_series

    def get_pvalues(self):
        X = self.right_hand_side
        y = self.left_hand_side
        X = np.column_stack((np.ones(X.shape[0]), X))

        XTVX = X.T @ self.V_inv @ X

        y_pred = np.dot(X, self.beta_gls)
        residuals = y - y_pred
        mse = residuals.T @ residuals/ (X.shape[0] - X.shape[1])

        t_stats = self.beta_gls / np.sqrt(np.diag(mse * np.linalg.inv(XTVX)))
        p_values = 2 * (1 - t.cdf(np.abs(t_stats), (X.shape[0] - X.shape[1])))

        p_values_series = pd.Series(p_values[0:], name="P-values for the corresponding coefficients")

        return p_values_series

    def get_wald_test_result(self, restriction_matrix):
        X = self.right_hand_side
        y = self.left_hand_side
        X = np.concatenate((np.ones((X.shape[0], 1)), self.right_hand_side), axis=1)
        R = np.asmatrix(restriction_matrix)

        n = X.shape[0]
        df2 = n - X.shape[1]
        residuals = y - np.dot(X, self.beta_gls)
        sse = np.dot(residuals.T, residuals)/df2

        RBr = R @ self.beta_gls
        df1 = R.shape[0]
        wald_one = R @ np.linalg.inv(X.T @ self.V_inv @ X) @ R.T
        wald_test = RBr @ np.linalg.inv(wald_one) @ RBr.T/ df1/ sse

        p_value = 1 - f.cdf(wald_test.item(), df1, df2)
        result_string = f"Wald: {wald_test.item():.3f}, p-value: {p_value:.3f}"
        return result_string

    def get_model_goodness_values(self):
        X = self.right_hand_side
        y = self.left_hand_side
        n = X.shape[0]
        X = np.column_stack((np.ones(n), X))

        sse = y.T @ self.V_inv @ X @ self.beta_gls
        sst = y.T @ self.V_inv @ y

        crs = 1 - sse / sst
        ars = 1 - (1 - crs) * (n - 1) / (n - X.shape[1])

        result_string = f"Centered R-squared: {crs:.3f}, Adjusted R-squared: {ars:.3f}"
        return result_string