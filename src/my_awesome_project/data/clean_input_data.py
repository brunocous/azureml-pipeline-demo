import pandas as pd


def clean(df: pd.DataFrame) -> pd.DataFrame:
    # not really cleaning, but you get the idea
    df["E"] = df["A"] + df["B"]
    return df
