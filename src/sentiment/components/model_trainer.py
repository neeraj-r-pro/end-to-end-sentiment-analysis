import sys

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from sentiment.exception import CustomException
from sentiment.logging import logging
from sentiment.entity.config_entity import ModelTrainerConfig
from sentiment.utils import save_object


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, X_train, y_train, X_test, y_test):
        try:
            logging.info("Model training started")

            model = LogisticRegression()

            model.fit(X_train, y_train)

            logging.info("Model training completed")

            y_pred = model.predict(X_test)

            accuracy = accuracy_score(y_test, y_pred)

            logging.info(f"Model Accuracy: {accuracy}")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=model
            )

            logging.info("Trained model saved successfully")

            return accuracy

        except Exception as e:
            raise CustomException(e, sys)