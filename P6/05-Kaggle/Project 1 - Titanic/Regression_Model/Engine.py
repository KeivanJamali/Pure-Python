import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import Information as info
from sklearn.metrics import accuracy_score, confusion_matrix, precision_recall_curve
from sklearn.metrics import classification_report
import statsmodels.api as sm
import seaborn as sns


class Engine:
    def __init__(self, data:pd.DataFrame):
        self.data = data

    def fit(self):
        self._set_setting()
        self._regression_model()

    def _set_setting(self):
        self.x = self.data[info.features].values
        self.y = self.data[info.target].values
        print(f"[INFO] Data splitted to X and Y.")

    def _regression_model(self):
        self.x = sm.add_constant(self.x)
        self.model = sm.Logit(self.y, self.x).fit() # Ordinary Least Square
        self.y_pred = self.model.predict(self.x)
        self.y_pred_label = (self.y_pred >= 0.5).astype(int)
        print(self.model.summary())
        print("Accuracy:", accuracy_score(self.y, self.y_pred_label))
        print("Confusion Matrix:\n", confusion_matrix(self.y, self.y_pred_label))
        print(classification_report(self.y, self.y_pred_label))

    def weight_plot(self, cons:bool=False, alpha=0.05):
        self.parameters_data = self.model.conf_int(alpha=alpha)
        self.parameters_data = pd.DataFrame(self.parameters_data, columns=["lower", "upper"], index=["cons"]+info.features)        
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
        self.parameters_data = pd.DataFrame(self.parameters_data, columns=["coef"], index=["cons"]+info.features)
        self.parameters_data.drop("cons", inplace=True)
        self.coefs = self.parameters_data["coef"]
        self.x_effects = self.data[self.parameters_data.index]
        self.effects = self.x_effects.multiply(self.coefs, axis=1)

        plt.figure(figsize=(10, 6))
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


