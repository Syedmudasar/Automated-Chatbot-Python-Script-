import pytest
from com_hrbot_logger.log import Log
from com_hrbot_constant.hrbot_config_mapper import HrBot_Config_mapper
import time
from com_htbot_utility.excel_reader import *
from allure_commons.types import AttachmentType
import allure
from analytics_module.conftest import *


logger = Log.get_logger()

@pytest.mark.usefixtures('setup')
class Test28:

    def test128_Verify_quick_action(self):
        driver = self.driver
        try:
            logger.info('enter user\'s credentials to login page')
            element = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_user_box"))
            element.send_keys(HrBot_Config_mapper.hrbot_config.get("username"))

            element = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_pass_box"))
            element.send_keys(HrBot_Config_mapper.hrbot_config.get("password"))
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

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('users_management')).click()
            logger.info('User has successfully clicked on user\'s  module')

            url = self.driver.current_url
            url1 = ExcelReader.read_excel().get('hrbot_users_url')
            if url:
                assert url == url1.replace('\n', '')
                logger.info('User has been navigated successfully to user\'s page')
            else:
                logger.info('User is not navigated to user\'s page')

            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('user_management'), 'visibility', driver)

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('activate_tab')).click()
            logger.info('User has successfully clicked on activate tab')

            time.sleep(2)
            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('deactivate_action')).click()
            logger.info('User has successfully clicked on deactivate from action column in order to deactivate profile')

            time.sleep(2)
            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('deactivate')).click()
            logger.info('User has successfully clicked on deactivate from action column in order to deactivate profile')

            time.sleep(2)
            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('confirmation_button')).click()
            logger.info('User has clicked on yes button on confirmation pop up')

            time.sleep(2)
            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('confirmation_message')).is_displayed()
            logger.info('User profile activated again a pup up is displayed on right corner')

        except Exception as e:
            allure.attach(driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            logger.error('An Error occurred in verify quick_action functionality')
            print(e)
            pytest.fail(e, pytrace=True)
