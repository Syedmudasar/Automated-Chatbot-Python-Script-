from selenium import webdriver
from com_hrbot_constant.constant import Constant
from com_hrbot_logger.log import Log
import time
from com_hrbot_constant.hrbot_config_mapper import *
import sys
import selenium.webdriver.chrome.service as service

logger = Log.get_logger()

class LaunchEnvironment:

    @staticmethod
    def launch_chrome(host_name):
        try:
            logger.info('Browser is being launched by driver')
            if host_name == 'chrome':
                print('--------hit url --------------')
                options = webdriver.ChromeOptions()
                options.add_argument('--no-sandbox')
                options.add_argument('--window-size=1520,1180')
                options.add_argument('--disable-gpu')
                driver = webdriver.Chrome(executable_path=Constant.chrom_driver, chrome_options=options)
                driver.get(HrBot_Config_mapper.hrbot_config.get('dev_url'))
                logger.info('Chrome Browser has been launched successfully')
                return driver
            else:
                logger.error('not found host name')
        except Exception as e:
            print("there is an exception while launching environment:  %s" % str(e))
            driver.save_screenshot(Constant.screen_shot_loc)
            print("there is an exception while launching environment")

    @staticmethod
    def launch_firefox(host_name):
        try:
            logger.info('Browser is being launched by driver')
            if host_name == 'firefox':
                driver = webdriver.firefox()
                driver.get(HrBot_Config_mapper.hrbot_config.get('dev_url'))
                logger.info('FireBox Browser has been successfully launched')
                return driver
            else:
                logger.error('not found host name')
        except Exception as e:
            print("there is an exception while launching environment", e)
            driver.save_screenshot(Constant.screen_shot_loc)
            print("there is an exception while launching environment")

    @staticmethod
    def launch_headless():
        try:
            options = webdriver.ChromeOptions()
            options.add_argument('--no-sandbox')
            options.add_argument('--window-size=1520,1180')
            options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            driver = webdriver.Chrome(executable_path=Constant.chrom_driver, options=options)
            driver.get(HrBot_Config_mapper.hrbot_config.get('dev_url'))
            logger.info('Chrome Browser has been launched successfully')
            return driver
        except Exception as e:
            print("there is an exception while launching environment", e)
            driver.save_screenshot(Constant.screen_shot_loc)
            print("there is an exception while launching environment")


