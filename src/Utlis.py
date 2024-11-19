import os
import sys
#We can use this for writting common function such as train_test_split function.
import numpy as np
import pandas as pd
import dill # type: ignore

from src.Exception import CustomException
from src.Logger import logging


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e,sys)