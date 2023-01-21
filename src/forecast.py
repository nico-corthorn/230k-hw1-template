"""
Optional module. 
I thought it could make sense a module
where all the vol forecasting functions are.
Feel free to use it, change it, or delete it.
"""

import pandas as pd

def forecast_vix(df: pd.DataFrame) -> pd.DataFrame:
    """ This one might be so easy you don't even need a function... """
    return df

def forecast_garch(df: pd.DataFrame) -> pd.DataFrame:
    """ You could return the same DataFrame with an extra column or
        change it to return a pandas Series. Whatever feels right for you.
    """
    return df

def forecast_har(df: pd.DataFrame) -> pd.DataFrame:
    return df
