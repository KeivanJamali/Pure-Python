import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


class Forcasting_Formulas:
    def __init__(self, data: pd.DataFrame) -> None:
        data2 = data.copy()
        data2.columns = [0, 1]
        self.data = data2

    def simple_moving_average(self, number_of_data: int, number_of_prediction: int) -> [pd.DataFrame, pd.DataFrame]:
        new_data = self.data.iloc[-number_of_data:, :]
        updated_data = self.data.iloc[:, :]
        for _ in range(number_of_prediction):
            predict = new_data.iloc[-number_of_data:, 1].mean()
            predict_data = pd.DataFrame({0: [new_data.iloc[-1, 0] + 1], 1: [predict]})
            new_data = new_data._append(predict_data, ignore_index=True)
            updated_data = updated_data._append(predict_data, ignore_index=True)
        new_data.index = range(1, 1 + len(new_data))
        return new_data, updated_data

    @staticmethod
    def plotting(data: pd.DataFrame, data_name: str) -> None:
        plt.scatter(data.iloc[:, 0], data.iloc[:, 1])
        plt.title(f"Domestic sale of Electricity from {data.iloc[0, 0]} to {data.iloc[-1, 0]}.")
        plt.xlabel("Year")
        plt.ylabel("Electricity (Million Kilowatt-hour)")
        if not os.path.exists(f"plots"):
            os.mkdir(f"plots")
        plt.savefig(f"plots/{data_name}.svg", format="svg")
        plt.show()
