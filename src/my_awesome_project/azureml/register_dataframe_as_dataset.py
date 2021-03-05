from azureml.core import Dataset, Workspace
from azureml.core.datastore import Datastore
import pandas as pd
import numpy as np


def register_dataframe_as_dataset() -> None:
    local_path = "data/"
    target_path = "random_data/"

    ws = Workspace.get(
        name="my_ws",
        subscription_id="111",
        resource_group="my_rg",
    )

    datastore = Datastore.get(workspace=ws, datastore_name="my_datastore")

    df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list("ABCD"))

    df.to_parquet(local_path, index=False)
    data_reference = datastore.upload(
        src_dir=local_path, target_path=target_path, overwrite=True
    )
    dataset = Dataset.Tabular.from_parquet_files(path=data_reference)
    dataset.register(workspace=ws, name="my_raw_dataset")


if __name__ == "__main__":
    register_dataframe_as_dataset()
