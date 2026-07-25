from sentiment.components.data_ingestion import DataIngestion
from sentiment.components.data_transformation import DataTransformation
from sentiment.logging import logging
from sentiment.exception import CustomException
import sys

if __name__ == "__main__":
    logging.info("The execution has started")

    try:
        data_ingestion = DataIngestion()

        train_data, test_data = data_ingestion.initiate_data_ingestion()

        logging.info("Data ingestion completed successfully")

        data_transformation = DataTransformation()

        X_train, y_train, X_test, y_test, preprocessor_path = (
            data_transformation.initiate_data_transformation(
                train_data,
                test_data
            )
        )

        logging.info("Data transformation completed successfully")

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)