# PyCaret Research-to-Production Template
This is a template for an end-to-end data science project using PyCaret for machine learning modeling (the research environment) and BentoML for model serving (the production environment).

**Author**: Arthur G.
***

## Main Project Dependencies
+ dvc == 2.12.1"
+ pytest == 7.1.2"
+ bentoml == 1.0.0rc3"
+ pycaret[full] == 2.3.10"
***

## Project Structure
------------
    ├── data
    │   ├── finalized        <- Data ready for modeling and retraining in production.
    │   ├── processed        <- Intermediate data that has been transformed.
    │   └── raw              <- The original, immutable data dump.
    │
    ├── conf                 <- Folder to store the main config.yaml file
    │   ├── __init__.py      <- Makes conf a Python module
    │   ├── config_core.py   <- Scripts to make config.yaml data importable. 
    │   └── config.yaml      <- Config file to store data, pipeline and model's related information.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── src                       <- Source code for use in this project.
    │   ├── __init__.py           <- Makes src a Python module
    │   ├── data_processing.py    <- Scripts to run the data processing define in the notebooks.
    │   └── train_pipeline.py     <- Scripts to train/retrain the model pipeline.
    │
    ├── tests                          <- Code for test data proc and train scripts.
    │   ├── __init__.py                <- Makes tests a Python module
    │   ├── test_data_processing.py    <- Test data processing script.
    │   └── test_train_pipeline.py     <- Test training script.
    │
    ├── bentofile.yaml     <- File used to build a deployable Bento API.
    ├── Pipfile            <- The requirements file for reproducing the environment
    ├── Makefile           <- Makefile with commands like `make install` or `make activate`
    ├── LICENSE            <- The specified LICENSE for the project.
    ├── README.md          <- The top-level README for developers using this project.
    └── service.py         <- File to run the BentoML server and make the trained model available.


--------

## Main Features
+ Research and production in one code base.
+ Just run one file to generate production-ready API with BentoML CLI.
+ Use Pipenv to ease the project dependencies management.
+ Manage code files as well as data and model files on the same project using DVC.