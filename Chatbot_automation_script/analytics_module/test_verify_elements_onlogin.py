import pytest
from com_hrbot_logger.log import Log
from com_hrbot_constant.hrbot_config_mapper import HrBot_Config_mapper
from com_htbot_utility.utility import Utility
from com_hrbot_constant.constant import *
from selenium import webdriver
from analytics_module.conftest import *
from allure_commons.types import AttachmentType
import allure


logger = Log.get_logger()

@pytest.mark.usefixtures("setup")
class Test2:

    def test_verify_login_content(self):
        try:
            logger.info('Verify the Telus international Logo, that is on left corner')
            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('logo1')).is_displayed()
            logger.info('Logo is displayed on login page')

            logger.info('Verify the input text box for login page')
            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('login_user_box')).is_displayed()
            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('login_pass_box')).is_displayed()
            logger.info('Input boxes are visible on login page ')

            logger.info('Verify the login button on login page ')
            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('login_button')).is_displayed()
            logger.info('Login button is visible there')

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            logger.error('An Error occurred in verify login content Test case')
            print(e)
            pytest.fail(e, pytrace=True)


