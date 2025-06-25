# Kidney-Disease-Classification

---

## Workflows

1. Update config.yanl
2. Update secrets.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml




## STEPS:

### Clone the repository

```bash
https://github.com/krishnaik06/Kidney-Disease-Classification-Deep-Learning-Project

```
---

### STEP 01 - Create a conda environment after opening the repository

```bash
conda create -n Kidney-Disease-Classification python=3.8 -y
conda activate Kidney-Disease-Classification

```
### STEP 02 - Install the requirements

```bash
pip install -r requirements.txt
```


## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)

##### cmd
-mlflow ui


### Dagshub
[Dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/chirag003214/Kidney-Disease-Classification.mlflow
MLFLOW_TRACKING_USERNAME=chirag003214
MLFLOW_TRACKING_PASSWORD=f92e4c8b3ec9f4390eb110baf4df4125dcb26a2b
python script.py 

Run this to export as env variables:


```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/chirag003214/Kidney-Disease-Classification.mlflow

export TRACKING_USERNAME=chirag003214

export MLFLOW_TRACKING_PASSWORD=f92e4c8b3ec9f4390eb110baf4df4125dcb26a2b


```


### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag


## About MLflow & DVC

MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & taging your model


DVC 

 - Its very lite weight for POC only
 - lite weight expriements tracker
 - It can perform Orchestration (Creating Pipelines)


