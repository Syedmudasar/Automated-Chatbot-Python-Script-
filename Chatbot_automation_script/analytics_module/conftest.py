import unittest
from selenium import webdriver
from com_hrbot_logger.log import Log
from com_hrbot_constant.hrbot_config_mapper import HrBot_Config_mapper
from com_htbot_utility.utility import Utility
from com_hrbot_constant.constant import *
from com_hrbot_modules.launchEnvironment import *
from com_hrbot_modules.launch_Environment1 import *
import pytest
import time



logger = Log.get_logger()
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--window-size=1520,1180')
options.add_argument('--disable-gpu')

@pytest.fixture(scope='class')
def setup(request):
    global driver
    try:
        logger.info('The Driver has started to open browser')
        try:
            driver = LaunchEnvironment.launch_chrome(HrBot_Config_mapper.hrbot_config.get("application_host"))
        except Exception as e:
            print('---------here is exception--------1', e)
        request.cls.driver = driver
        time.sleep(5)
        logger.info('browser has launched successfully')
        yield driver
        logger.info('Test Case has Finished successfully')
        driver.quit()
        logger.info('Here Browser has closed successfully')
    except Exception as e:
        print(e)

@pytest.fixture(scope='class')
def setup1(request):
    global driver
    try:
        logger.info('the driver has started to open browser 1')
        try:
            driver = LaunchEnvironment1.open_google_mail(HrBot_Config_mapper.hrbot_config.get('application_host'))
        except Exception as e:
            print('------------here is exception--------2', e)
        request.cls.driver = driver
        yield driver
        logger.info('Test Case has Finished successfully')
        driver.quit()
        logger.info('Here Browser has closed successfully')
    except Exception as e:
        print(e)
