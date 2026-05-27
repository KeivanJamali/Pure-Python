import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import Information as info
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm
from statsmodels.regression.linear_model import OLS
import seaborn as sns


class Engine:
    def __init__(self, data:pd.DataFrame):
        self.data = data

    def fit(self):
        self._set_setting()
        self._regression_model()

    def _set_setting(self):
        self.y = self.data[info.target].values
        self.x = self.data.drop(info.target, axis=1).values
        self.features = list(self.data.drop(info.target, axis=1).columns)
        print(f"[INFO] Data splitted to X and Y.")

    def _regression_model(self):
        self.x = sm.add_constant(self.x)
        # self.model = sm.OLS(self.y, self.x).fit() # Ordinary Least Square
        self.model = OLS(self.y, self.x) # Ordinary Least Square
        self.model = self.model.fit_regularized(method='elastic_net', alpha=100, L1_wt=0.5)
        # print(self.model.summary())
        coef = pd.Series(self.model.params, index=["cons"]+self.features)
        print("\nCoefficients (Lasso):")
        print(coef)
        # Get predictions
        self.y_pred = np.dot(self.x, self.model.params)

        # Calculate R²
        ss_total = np.sum((self.y - np.mean(self.y)) ** 2)
        ss_residual = np.sum((self.y - self.y_pred) ** 2)
        r2 = 1 - ss_residual / ss_total

        # Adjusted R²
        n = self.x.shape[0]
        p = self.x.shape[1] - 1  # subtract intercept
        r2_adj = 1 - (1 - r2) * (n - 1) / (n - p - 1)

        print(f"\nR²: {r2:.4f}")
        print(f"Adjusted R²: {r2_adj:.4f}")

    def weight_plot(self, cons:bool=False, alpha=0.05):
        self.parameters_data = self.model.conf_int(alpha=alpha)
        self.parameters_data = pd.DataFrame(self.parameters_data, columns=["lower", "upper"], index=["cons"]+self.features)        
        self.parameters_data["coef"] = self.model.params
        if not cons:
            self.parameters_data.drop("cons", inplace=True)

        plt.figure(figsize=(8, len(self.parameters_data)*0.6))
        plt.errorbar(x=self.parameters_data['coef'], y=self.parameters_data.index,
                    xerr=[self.parameters_data['coef'] - self.parameters_data['lower'], 
                          self.parameters_data['upper'] - self.parameters_data['coef']],
                    fmt='o', color='navy', ecolor='skyblue', capsize=4)

        plt.axvline(x=0, color='gray', linestyle='--')  # zero line
        plt.title(f'Feature Effects with {int(100-100*alpha)}% Confidence Intervals')
        plt.xlabel('Coefficient Estimate')
        plt.ylabel('Feature')
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def effect_plot(self, data_id:int=None):
        self.parameters_data = self.model.params
        self.parameters_data = pd.DataFrame(self.parameters_data, columns=["coef"], index=["cons"]+self.features)
        self.test = ["cons"]+self.features
        self.parameters_data.drop("cons", inplace=True, axis=0)
        self.coefs = self.parameters_data["coef"]
        self.x_effects = self.data[self.parameters_data.index]
        self.effects = self.x_effects.multiply(self.coefs, axis=1)

        plt.figure(figsize=(10, 60))
        sns.boxplot(data=self.effects, orient="h", color="skyblue", showfliers=True)
        if data_id:
            datapoint_effects = self.effects.loc[data_id]
            for i, (feature_name, effect_value) in enumerate(datapoint_effects.items()):
                plt.plot(effect_value, i, 'rx', markersize=10, label='Selected datapoint' if i == 0 else "")  # add label only once

        plt.title("Feature Effect Plot")
        plt.xlabel("Effect on Prediction")
        plt.ylabel("Feature")
        plt.grid()
        plt.tight_layout()
        plt.show()


