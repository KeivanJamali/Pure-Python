import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import r2_score

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
        return new_data.iloc[-number_of_prediction:, 1], updated_data

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
        return new_data.iloc[-number_of_prediction:, 1], updated_data

    @staticmethod
    def _exponential_smoothing_myself(data: pd.DataFrame, alpha: float) -> float:
        """
        Calculates the exponential smoothing of the data and predicts the future value.
        """
        initial_prediction = data.iloc[9:, 1].mean()
        predict = 0
        new_data = data.iloc[:, :].copy()
        for i in range(len(data)):
            predict = new_data.iloc[i, 1] * alpha + (1 - alpha) * initial_prediction
            initial_prediction = predict
        return predict

    def serious_exponential_smoothing_myself(self, all_data: list, alpha: float) -> [pd.DataFrame, pd.DataFrame]:
        """
        Calculates the exponential smoothing of the data and predicts the future values.
        """
        predicted_data = pd.DataFrame({0: [], 1: []})
        total_data = self.data.copy()
        for new_data in all_data:
            the_new_data = self._exponential_smoothing_myself(new_data, alpha)
            predicted_data = predicted_data._append(pd.DataFrame({0: [new_data.iloc[-1, 0] + 1], 1: [the_new_data]}),
                                                    ignore_index=True)
        total_data = total_data._append(predicted_data, ignore_index=True)
        predicted_data.index = range(1, 1 + len(predicted_data))
        total_data.index = range(1, 1 + len(total_data))
        return predicted_data.iloc[-len(all_data):, 1], total_data

    def exponential_smoothing(self, number_of_prediction: int, alpha: float, beta: float = None):
        """
        Generates a prediction using exponential smoothing.

        Args:
            number_of_prediction (int): The number of steps to forecast.
            alpha (float): The smoothing level.
            beta (float, optional): The smoothing trend. Only for Trend_adjusted method. Defaults to None.

        Returns:
            pandas.DataFrame: A DataFrame containing the predicted data.
        """
        predicted_data = pd.DataFrame({0: [], 1: []})
        data = self.data.copy()
        data.iloc[:, 0] = pd.to_datetime(data.iloc[:, 0])
        data.set_index(0, inplace=True)
        data2 = self.data.copy()
        model = ExponentialSmoothing(self.data[1], trend="add", initialization_method="estimated", seasonal_periods=12,
                                     use_boxcox=True).fit(smoothing_level=alpha, smoothing_trend=beta)
        prediction = model.forecast(steps=number_of_prediction)
        for i in range(len(prediction)):
            predicted_data = predicted_data._append(
                pd.DataFrame({0: [data2.iloc[-1, 0] + 1 + i], 1: [prediction.iloc[i]]}),
                ignore_index=True)
        data2 = data2._append(predicted_data, ignore_index=True)
        data2.index = range(1, 1 + len(data2))
        return predicted_data.iloc[-number_of_prediction:, 1], data2

    def score(self, method: list, true_val, predict_val) -> float:
        """
        Calculate the score using different methods.

        Parameters:
            method (list): A list of strings indicating the methods to be used for calculating the score. Valid options are "MAE", "MSE", R2, and "MAD".
            true_val: The true values.
            predict_val: The predicted values.

        Returns:
            float: The calculated score.

        Raises:
            None
        """
        error = {}
        if "MAE" in method:
            error["MAE"] = mean_absolute_error(true_val, predict_val)
        if "MSE" in method:
            error["MSE"] = mean_squared_error(true_val, predict_val, squared=True)
        if "MAD" in method:
            error["MAD"] = mean_absolute_percentage_error(true_val, predict_val)
        if "R2" in method:
            error["R2"] = r2_score(true_val, predict_val)

        return error

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
