import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import hydra
import numpy as np
import pandas as pd
from omegaconf import DictConfig
from src.train_pipeline import run_training
from sklearn.pipeline import Pipeline


@hydra.main(version_base=None, config_path="../conf/", config_name="config.yaml")
def test_train_pipeline_func(config: DictConfig) -> None:
    """
    This function tests if the train pipeline function is working properly,
    producing a trained pipeline.
    """
    pipeline = run_training(config)

    assert type(pipeline) == type(Pipeline)