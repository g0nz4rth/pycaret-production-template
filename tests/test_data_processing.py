import os, sys

from py import process
sys.path.insert(1, os.path.abspath('.'))

import hydra
import numpy as np
import pandas as pd
from omegaconf import DictConfig
from src.data_processing import *


@hydra.main(version_base=None, config_path="../conf/", config_name="config.yaml")
def test_data_processing_func(config: DictConfig) -> None:
    """
    This function tests if the current data processing function
    is producting the right output.
    """
    # correct template
    template = {
        'pickup_year': np.dtype('int64'),
        'pickup_month': np.dtype('int64'),
        'pickup_dayofyear': np.dtype('int64'),
        'pickup_dayofweek': np.dtype('int64'),
        'pickup_hour': np.dtype('int64'),
        'is_holiday': np.dtype('int64'),
        'passenger_count': np.dtype('int64'),
        'pickup_latitude': np.dtype('float64'),
        'pickup_longitude': np.dtype('float64'),
        'dropoff_latitude': np.dtype('float64'),
        'dropoff_longitude': np.dtype('float64'),
        'trip_distance_km': np.dtype('float64'),
        'fare_amount': np.dtype('float64')
    }

    processed_data = process_data(config.raw.path)

    assert processed_data.dtypes.to_dict() == template