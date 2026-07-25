import sys

import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline

from sentiment.exception import CustomException
from sentiment.logging import logging
from sentiment.entity.config_entity import DataTransformationConfig
from sentiment.utils import save_object


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        try:
            logging.info("Data Transformation initiated")

            preprocessor = Pipeline(
                steps=[
                    ("tfidf", TfidfVectorizer())
                ]
            )

            logging.info("TF-IDF Pipeline Created")

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):
        try:
            # Read the datasets
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            # Get the preprocessing pipeline
            preprocessing_obj = self.get_data_transformer_object()

            target_column_name = "sentiment"

            # Separate features and target
            input_feature_train_df = train_df.drop(columns=target_column_name, axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=target_column_name, axis=1)
            target_feature_test_df = test_df[target_column_name]

            # Transform the review text
            input_feature_train_arr = preprocessing_obj.fit_transform(
                input_feature_train_df["review"]
            )

            input_feature_test_arr = preprocessing_obj.transform(
                input_feature_test_df["review"]
            )

            # Save the preprocessor
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            logging.info("Preprocessor object saved")

            return (
                input_feature_train_arr,
                target_feature_train_df.to_numpy(),
                input_feature_test_arr,
                target_feature_test_df.to_numpy(),
                self.data_transformation_config.preprocessor_obj_file_path,
            )

        except Exception as e:
            raise CustomException(e, sys)