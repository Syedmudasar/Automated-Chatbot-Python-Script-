import pytest
from com_hrbot_logger.log import Log
from com_hrbot_constant.hrbot_config_mapper import HrBot_Config_mapper
from com_hrbot_constant.constant import *
from com_htbot_utility.excel_reader import *
from analytics_module.conftest import *
from allure_commons.types import AttachmentType
import allure
import time

logger = Log.get_logger()


@pytest.mark.usefixtures('setup')
class Test33:

    def test33_Verify_users_setting_disable(self):
        driver = self.driver
        try:
            logger.info('enter user\'s credentials to login page')
            element = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_user_box"))
            element.send_keys(HrBot_Config_mapper.hrbot_config.get("Viewer_user"))

            element = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_pass_box"))
            element.send_keys(HrBot_Config_mapper.hrbot_config.get("Viewer_password"))
            logger.info('User has successfully entered credentials')

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_button")).click()
            logger.info('User has successfully clicked on login button')

            logger.info('Waiting for the element')
            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('conversation_reports'), 'visibility', driver)

            url = self.driver.current_url
            if url:
                assert url == ExcelReader.read_excel().get("hrbot_homepage_url")
                logger.info('User has been navigated successfully to home page')
            else:
                logger.info('User is not navigated to home page')

            flag = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('users')).is_enabled()
            if flag:
                logger.info('Users module is not disable as expected for viewer')
            else:
                logger.info('User module is disable as expected for viewer')

            flag = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('setting_module')).is_enabled()
            if flag:
                logger.info('User setting is not disable as expected for viewer')
            else:
                logger.info('User setting is disable as expected for viewer')

        except Exception as e:
            logger.info('An exception occurred in verify users and setting module 33')
            allure.attach(self.driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            print(e)
            pytest.fail(e, pytrace=True)
