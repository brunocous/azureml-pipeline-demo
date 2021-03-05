from typing import Any
import pandas as pd
from catboost import Pool, CatBoostRegressor


def train_model(data: pd.DataFrame, epochs: int) -> CatBoostRegressor:
    train_pool = Pool(data.drop("A", axis=1), data["A"], cat_features=[2, 4])

    model = CatBoostRegressor(
        iterations=epochs,
        depth=2,
        learning_rate=1,
        loss_function="Logloss",
        verbose=True,
    )

    model.fit(train_pool)
    return model
