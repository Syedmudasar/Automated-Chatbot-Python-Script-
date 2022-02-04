import pytest
from com_hrbot_logger.log import Log
from com_hrbot_constant.hrbot_config_mapper import HrBot_Config_mapper
from com_hrbot_constant.constant import *
from analytics_module.conftest import *
from allure_commons.types import AttachmentType
import allure
import time


logger = Log.get_logger()

@pytest.mark.usefixtures('setup')
class Test34:

    def test34_Verify_Editor_privilege(self):
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
            Utility.explicit_Wait(HrBot_Config_mapper.hrbot_locators.get('conversation_reports'), self.driver)

            url = self.driver.current_url
            if url:
                assert url == ExcelReader.read_excel().get("hrbot_homepage_url")
                logger.info('User has been navigated successfully to home page')
            else:
                logger.info('User is not navigated to home page')


        except Exception as e:
            logger.info('An exception occurred in verify Editor privilege 34')
            allure.attach(self.driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            print(e)
            pytest.fail(e, pytrace=True)
