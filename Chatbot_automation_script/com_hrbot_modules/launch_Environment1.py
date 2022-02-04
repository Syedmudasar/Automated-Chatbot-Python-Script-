from selenium import webdriver
from com_hrbot_constant.constant import Constant
from com_hrbot_logger.log import Log
import time
from com_hrbot_constant.hrbot_config_mapper import *
import sys
import selenium.webdriver.chrome.service as service

logger = Log.get_logger()

class LaunchEnvironment1:

    @staticmethod
    def open_google_mail(host_name):
        try:
            logger.info('Browser is being launched by driver')
            if host_name == 'chrome':
                print('--------hit url 1 --------------')
                options = webdriver.ChromeOptions()
                options.add_argument('--no-sandbox')
                options.add_argument('--window-size=1520,1180')
                options.add_argument('--disable-gpu')
                driver = webdriver.Chrome(executable_path=Constant.chrom_driver, chrome_options=options)
                driver.get("http://mail.google.com/a/telusinternational.com")
                time.sleep(5)
                logger.info('Chrome Browser has been launched successfully')
                return driver
            else:
                logger.error('not found host name')
        except Exception as e:
            print("there is an exception while launching environment:  %s" % str(e))
            driver.save_screenshot(Constant.screen_shot_loc)
            print("there is an exception while launching environment")


