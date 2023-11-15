import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


class Forcasting_Formulas:
    """
    Initializes the object with the given data.

    Parameters:
        data (pd.DataFrame): The data to be stored in the object.

    Returns:
        None
    """

    def __init__(self, data: pd.DataFrame) -> None:
        data2 = data.copy()
        data2.columns = [0, 1]
        self.data = data2

    def simple_moving_average(self, number_of_data: int, number_of_prediction: int) -> [pd.DataFrame, pd.DataFrame]:
        """
        Calculates the simple moving average of a given number of data points and predicts the moving average for a given number of future data points.

        Parameters:
            number_of_data (int): The number of data points to consider for calculating the moving average.
            number_of_prediction (int): The number of future data points for which to predict the moving average.

        Returns:
            Tuple[pd.DataFrame, pd.DataFrame]: A tuple containing two pandas DataFrames. The first DataFrame represents the new data with the predicted moving averages, and the second DataFrame represents the updated data with the predicted moving averages appended.
        """
        new_data = self.data.iloc[-number_of_data:, :]
        updated_data = self.data.iloc[:, :]
        for _ in range(number_of_prediction):
            predict = new_data.iloc[-number_of_data:, 1].mean()
            predict_data = pd.DataFrame({0: [new_data.iloc[-1, 0] + 1], 1: [predict]})
            new_data = new_data._append(predict_data, ignore_index=True)
            updated_data = updated_data._append(predict_data, ignore_index=True)
        new_data.index = range(1, 1 + len(new_data))
        return new_data, updated_data

    def weighted_moving_average(self, number_of_data: int, weights: list, number_of_prediction: int) -> [pd.DataFrame,
                                                                                                         pd.DataFrame]:
        """
        Calculates the weighted moving average of a given number of data points and predicts the future values using the provided weights.

        Parameters:
            number_of_data (int): The number of data points to consider for the moving average calculation.
            weights (list): The weights to use in the weighted average calculation. [earlier year, ..., later year]
            number_of_prediction (int): The number of future values to predict.

        Returns:
            pd.DataFrame: The new data frame containing the predicted values.
            pd.DataFrame: The updated data frame including the predicted values.
        """
        new_data = self.data.iloc[-number_of_data:, :]
        updated_data = self.data.iloc[:, :]
        for _ in range(number_of_prediction):
            predict = np.average(new_data.iloc[-number_of_data:, 1], weights=weights)
            predict_data = pd.DataFrame({0: [new_data.iloc[-1, 0] + 1], 1: [predict]})
            new_data = new_data._append(predict_data, ignore_index=True)
            updated_data = updated_data._append(predict_data, ignore_index=True)
        new_data.index = range(1, 1 + len(new_data))
        return new_data, updated_data

    def exponential_smoothing(self):
        pass

    def trend_adjusted_exponential_smoothing(self):
        pass

    @staticmethod
    def plotting(data: pd.DataFrame, data_name: str) -> None:
        """
        Generate a scatter plot of the given data.

        Parameters:
            data (pd.DataFrame): The data to be plotted.
            data_name (str): The name of the data.

        Returns:
            None
        """
        plt.scatter(data.iloc[:, 0], data.iloc[:, 1])
        plt.title(f"Domestic sale of Electricity from {data.iloc[0, 0]} to {data.iloc[-1, 0]}.")
        plt.xlabel("Year")
        plt.ylabel("Electricity (Million Kilowatt-hour)")
        if not os.path.exists(f"plots"):
            os.mkdir(f"plots")
        plt.savefig(f"plots/{data_name}.svg", format="svg")
        plt.show()
