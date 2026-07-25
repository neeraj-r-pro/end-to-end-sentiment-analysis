from sentiment.components.data_ingestion import DataIngestion
from sentiment.components.data_transformation import DataTransformation
from sentiment.components.model_trainer import ModelTrainer
from sentiment.logging import logging
from sentiment.exception import CustomException
import sys

if __name__ == "__main__":
    logging.info("The execution has started")

    try:
        # Data Ingestion
        data_ingestion = DataIngestion()

        train_data, test_data = data_ingestion.initiate_data_ingestion()

        logging.info("Data ingestion completed successfully")

        # Data Transformation
        data_transformation = DataTransformation()

        X_train, y_train, X_test, y_test, preprocessor_path = (
            data_transformation.initiate_data_transformation(
                train_data,
                test_data
            )
        )

        logging.info("Data transformation completed successfully")

        # Model Training
        model_trainer = ModelTrainer()

        accuracy = model_trainer.initiate_model_trainer(
            X_train,
            y_train,
            X_test,
            y_test
        )

        logging.info("Model training completed successfully")

        print(f"Model Accuracy: {accuracy * 100:.2f}%")
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)