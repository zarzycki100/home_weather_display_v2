import logging
import os
from dotenv import load_dotenv


class Logger:
    def __init__(self) -> None:
        load_dotenv()
        logging.basicConfig(filename=os.getenv('LOGGER_FILE'), level=logging.DEBUG, format="%(asctime)s %(message)s")

    @staticmethod
    def debug(message):
        logging.debug(message)

    @staticmethod
    def info(message):
        logging.info(message)

    # @staticmethod
    # def warning(message):
    #     logging.warning(message)
    # @staticmethod
    # def warning(message):
    #     logging.warning(message)
    #     logging.warning("The program may not function properly")
    #     logging.error("The program encountered an error")
    #     logging.critical("The program crashed")



