import os
import sys

import pandas as pd
from sklearn.model_selection import train_test_split

from sentiment.exception import CustomException
from sentiment.logging import logging
from sentiment.entity.config_entity import DataIngestionConfig
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")

        try:
            df = pd.read_csv("notebook/IMDB Dataset.csv")
            logging.info("Dataset read into pandas DataFrame")

            os.makedirs(
                os.path.dirname(self.ingestion_config.train_data_path), 
                exist_ok=True
            )

            df.to_csv(
                self.ingestion_config.raw_data_path,
                index=False,
                header=True
            )

            logging.info("Raw dataset saved in artifacts folder")

            logging.info("Train-test split initiated")

            train_set, test_set = train_test_split(
                df,
                test_size=0.2,
                random_state=42
            )

            logging.info("Train-test split completed")
            train_set.to_csv(
                self.ingestion_config.train_data_path,
                index=False,
                header=True
            )

            test_set.to_csv(
                self.ingestion_config.test_data_path,
                index=False,
                header=True
            )

            logging.info("Train and test datasets saved successfully")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)