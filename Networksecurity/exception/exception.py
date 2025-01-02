import sys
import logging

# Mocking the logger for this example
class Logger:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def info(self, message):
        self.logger.info(message)

logger = Logger()

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details):
        """
        Custom exception class for handling network security errors.

        Args:
            error_message (str): The error message.
            error_details (sys): The sys module to extract traceback details.
        """
        self.error_message = error_message
        _, _, exc_tb = error_details.exc_info()
        if exc_tb:
            self.lineno = exc_tb.tb_lineno
            self.file_name = exc_tb.tb_frame.f_code.co_filename
        else:
            self.lineno = None
            self.file_name = None

    def __str__(self):
        return (
            f"Error occurred in python script name [{self.file_name}] "
            f"line number [{self.lineno}] error message [{self.error_message}]"
        )

if __name__ == '__main__':
    try:
        logger.info('Enter the try block')
        a = 1 / 0
        print('This will not be printed', a)
    except Exception as e:
        raise NetworkSecurityException(str(e), sys)
