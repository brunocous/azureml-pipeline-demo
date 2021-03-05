# azureml-pipeline-demo
Example Azure ML pipeline batch flow.

This code will not run out-of-the-box. You need to change the workspace and datastore config first probably.

This repo is to support a Medium article.

## Get started
Make sure you have a virtual environment installed and activated.
Then simply,
````
pip install -r requirements.txt
````

To upload data,
```
python src/my_awesome_project/azureml/register_dataframe_as_dataset.py
```

To define and trigger a pipeline,
```
python src/my_awesome_project/azureml/create_and_trigger_pipeline.py
```