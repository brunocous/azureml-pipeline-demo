from azureml.core import Dataset, Workspace
from azureml.core.datastore import Datastore
from azureml.core.compute import ComputeTarget
from azureml.core.experiment import Experiment
from azureml.core.runconfig import RunConfiguration
from azureml.data.output_dataset_config import OutputFileDatasetConfig
from azureml.pipeline.core.pipeline import Pipeline
from azureml.pipeline.steps import PythonScriptStep
from pathlib import Path
from my_awesome_project.azureml import aml_clean_data, aml_train_model
import my_awesome_project


def create_and_trigger_pipeline() -> None:
    ws = Workspace.get(
        name="my_ws",
        subscription_id="111",
        resource_group="my_rg",
    )
    datastore = Datastore.get(workspace=ws, datastore_name="my_datastore")

    input_data = Dataset.get_by_name(workspace=ws, name="my_raw_data")
    clean_data = (
        OutputFileDatasetConfig(
            name="my_clean_data",
            destination=(datastore, "path/on/blob/to/write/clean/data/to"),
        )
        .as_upload(overwrite=True)
        .register_on_complete(name="my_clean_data")
    )

    src_dir = Path(my_awesome_project.__file__).parent.parent
    clean_m_path = Path(aml_clean_data.__file__).relative_to(src_dir)
    train_m_path = Path(aml_train_model.__file__).relative_to(src_dir)
    clean_step = PythonScriptStep(
        name="clean data",
        script_name=str(clean_m_path),
        source_directory=src_dir,
        runconfig=RunConfiguration(),
        inputs=[input_data.as_named_input("my_raw_data").as_mount()],
        outputs=[clean_data],
        compute_target=ComputeTarget(workspace=ws, name="small_cluster"),
        allow_reuse=True,
    )
    train_step = PythonScriptStep(
        name="train_model",
        script_name=str(train_m_path),
        source_directory=src_dir,
        runconfig=RunConfiguration(),
        arguments=["--epochs", "5"],
        inputs=[clean_data.as_input()],
        outputs=[],
        compute_target=ComputeTarget(workspace=ws, name="small_cluster"),
        allow_reuse=True,
    )

    exp = Experiment(workspace=ws, name="my_experiment")
    pipeline = Pipeline(ws, steps=[clean_step, train_step])
    run = pipeline.submit(experiment_name=exp.name)
    run.wait_for_completion(raise_on_error=True)


if __name__ == "__main__":
    create_and_trigger_pipeline()
