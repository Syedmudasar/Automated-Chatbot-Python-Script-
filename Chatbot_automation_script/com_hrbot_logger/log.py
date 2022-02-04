import logging
from selenium import webdriver
# import unittest
# import sys
from com_hrbot_constant.constant import Constant
# import HtmlTestRunner
from logging import Formatter

class Log:

    @staticmethod
    def get_logger():
        logger = logging.getLogger(__name__)
        if not logger.hasHandlers():
            logger.setLevel(logging.DEBUG)

            logging.basicConfig(filename=Constant.log_file,
                                format='%(asctime)s -%(levelname)s - %(message)s',
                                datefmt='')

            s_handler = logging.StreamHandler()
            s_handler.setLevel(logging.DEBUG)

            # formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            # s_handler.setFormatter(formatter)

            logger.addHandler(s_handler)

        return logger
