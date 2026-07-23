import sys

from sentiment.logging import logging
from sentiment.exception import CustomException


try:
    a = 10
    b = 0
    print(a / b)

except Exception as e:
    logging.info("Divide by zero error")
    raise CustomException(e, sys)