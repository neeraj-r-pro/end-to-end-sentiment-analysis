import sys
import pandas as pd

from sentiment.exception import CustomException
from sentiment.utils import load_object
from sentiment.entity.config_entity import (
    DataTransformationConfig,
    ModelTrainerConfig,
)

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, text):
        try:
            preprocessor = load_object(
                DataTransformationConfig().preprocessor_obj_file_path
            )

            model = load_object(
                ModelTrainerConfig().trained_model_file_path
            )

            features = pd.DataFrame(
                {
                    "review": [text]
                }
            )

            data_scaled = preprocessor.transform(features["review"])

            prediction = model.predict(data_scaled)

            return prediction[0]

        except Exception as e:
            raise CustomException(e, sys)