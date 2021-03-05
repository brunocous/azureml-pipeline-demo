import os
from azureml.core import Run
from my_awesome_project.data.clean_input_data import clean

if __name__ == "__main__":
    run = Run.get_context()
    raw_df = run.input_datasets["my_raw_dataset"].to_pandas_dataframe()

    clean_df = clean(raw_df)
    mounted_output_dir = run.output_datasets["my_clean_dataset"]
    os.makedirs(os.path.dirname(mounted_output_dir), exist_ok=True)
    clean_df.to_parquet(mounted_output_dir)
