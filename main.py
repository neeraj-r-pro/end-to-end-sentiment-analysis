from sentiment.components.data_ingestion import DataIngestion
from sentiment.logging import logging
from sentiment.exception import CustomException
import sys

if __name__ == "__main__":
    logging.info("The execution has started")

    try:
        data_ingestion = DataIngestion()

        train_data, test_data = data_ingestion.initiate_data_ingestion()

        logging.info("Data ingestion completed successfully")

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)