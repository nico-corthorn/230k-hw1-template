# Random optional module. Create as many as you think appropriate.
import pandas as pd

def compute_cumulative_returns(df: pd.DataFrame):
    return df.returns.cumprod()

