import pandas as pd
import numpy as np
import scipy


def drawdown(return_series: pd.Series) -> pd.DataFrame:
    """
    Takes a time series of asset returns
    Computes and returns a DataFrame that contains:
    the wealth index
    the previous peaks
    percent drawdown
    """
    wealth_index = 1000 * (1 + return_series).cumprod()
    previous_peaks = wealth_index.cummax()
    drawdowns = (wealth_index - previous_peaks) / previous_peaks
    return pd.DataFrame({
        "wealth": wealth_index,
        "peaks": previous_peaks,
        "drawdown": drawdowns})


def get_ffme_returns() -> pd.DataFrame:
    """
    Load the Fama_French Dataset for the returns of the Top and Bottom Deciles by MarketCap
    """
    me_m = pd.read_csv("02- portfolios_formed_on_ME_monthly_EW.csv", header=0, index_col=0, na_values=-99.99)
    rets = me_m[["Lo 10", "Hi 10"]]
    rets.columns = ["SmallCap", "LargeCap"]
    rets /= 100
    rets.index = pd.to_datetime(rets.index, format="%Y%m").to_period("M")
    return rets


def get_hfi_returns() -> pd.DataFrame:
    """
    load and format EDHEC hedge fund index returns
    """
    hfi = pd.read_csv("Data/edhec-hedgefundindices.csv", header=0, index_col=0, parse_dates=True)
    hfi /= 100
    hfi.index = hfi.index.to_period("M")
    return hfi


def semideviation(r: pd.DataFrame) -> pd.DataFrame:
    """it returns semideviations aka negetive semideviation of r
    r must be a series or a dataframe
    """
    is_negetive = r < 0
    return r[is_negetive].std(ddof=0)


def skewness(r: pd.DataFrame) -> int:
    """
    :param r: all the data as DateFrame
    :return: skewness
    """
    demeaned = r - r.mean()
    sigma = r.std(ddof=0)  # Population
    exp = (demeaned ** 3).mean()
    return exp / (sigma ** 3)


def kurtosis(r):
    """

    :param r: all the data as DateFrame
    :return: kurtosis
    """
    demeaned = r - r.mean()
    sigma = r.std(ddof=0)  # Population
    exp = (demeaned ** 4).mean()
    return exp / (sigma ** 4)


def is_normal(r, level=0.01):
    """
    check if the DataFrame has normal distribution or not.
    :param r: all the data as DateFrame
    :param level: estimation level
    :return: True or False
    """
    statics, p_value = scipy.stats.jarque_bera(r)
    return p_value > level


def var_historic(r: pd.DataFrame, level=5):
    """
    VaR Historic
    :param r:
    :param level:
    :return:
    """
    if isinstance(r, pd.DataFrame):
        return r.aggregate(var_historic, level=level)
    elif isinstance(r, pd.Series):
        return -np.percentile(r, level)
    else:
        raise TypeError("Expected r to be Series or DataFrame")


def var_gaussian(r: pd.DataFrame, level=5, modified=False) -> pd.DataFrame:
    """
    Parametric gaussian
    :param r: DataFrame
    :param level: percent last
    :return: Parametric Gaussian VaR
    """
    # compute Z score
    z = scipy.stats.norm.ppf(level / 100)
    if modified:
        s = skewness(r)
        k = kurtosis(r)
        z = (z +
             (z ** 2 - 1) * s / 6 +
             (z ** 3 - 3 * z) * (k - 3) / 24 -
             (2 * z ** 3 - 5 * z) * (s ** 2) / 36
             )

    return -((r.mean()) + z * r.std(ddof=0))


def cvar_historic(r: pd.DataFrame, level: int = 5) -> pd.DataFrame:
    """
    comutes the conditional VaR of Series or DataFram
    :param r: Data
    :param level:
    :return:
    """
    if isinstance(r, pd.DataFrame):
        return r.aggregate(cvar_historic, level=level)
    elif isinstance(r, pd.Series):
        is_beyond = r <= -var_historic(r, level=level)
        return -r[is_beyond].mean()
    else:
        raise TypeError("Expected r to be Series or DataFrame")
