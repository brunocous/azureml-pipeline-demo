from argparse import ArgumentParser
from azureml.core import Run
from my_awesome_project.ml.model import train_model

if __name__ == "__main__":
    run = Run.get_context()
    ap = ArgumentParser()
    ap.add_argument("--epochs", default=10)
    args = ap.parse_args()

    clean_df = run.input_datasets["my_clean_data"].to_pandas_dataframe()
    trained_model = train_model(data=clean_df, epochs=args.epochs)
    trained_model.save("./outputs/model")  # /outputs is important
    run.register_model(name="my_model", path="outputs/model")
