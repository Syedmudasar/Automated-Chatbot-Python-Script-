import pytest
from com_hrbot_logger.log import *
from com_hrbot_constant.hrbot_config_mapper import *
from com_htbot_utility.utility import *
from com_htbot_utility.excel_reader import *
from analytics_module.conftest import *
from allure_commons.types import AttachmentType
import allure
import time

logger = Log.get_logger()

@pytest.mark.usefixtures('setup')
class Test18:

    def test18_Verify_all_elements_popup_on_invite_user_screen(self):
        driver = self.driver
        try:
            logger.info('enter user\'s credentials to login page')
            element = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_user_box"))
            element.send_keys(HrBot_Config_mapper.hrbot_config.get("username"))

            element = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_pass_box"))
            element.send_keys(HrBot_Config_mapper.hrbot_config.get("password"))
            logger.info('User has successfully entered credentials')

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_button")).click()
            logger.info('User has successfully clicked on login button')

            logger.info('Waiting for the element')
            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('conversation_reports'), 'visibility', driver)

            url = self.driver.current_url
            url1 = ExcelReader.read_excel().get("hrbot_homepage_url")
            if url:
                assert url == url1.replace('\n', '')
                logger.info('User has been navigated successfully to home page')
            else:
                logger.info('User is not navigated to home page')

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('users_management')).click()
            logger.info('User has successfully clicked on user\'s setting module')

            url = self.driver.current_url
            url1 = ExcelReader.read_excel().get("hrbot_users_url")
            if url:
                assert url == url1.replace('\n', '')
                logger.info('User has been navigated successfully to user\'s page')
            else:
                logger.info('User is not navigated to user\'s page')

            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('user_management'), 'visibility', self.driver)

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('invite_users_button')).click()
            logger.info('user has clicked successfully on invite user button')

            # validate all elements are visible on invite user screen
            logger.info('let\'s start validate the elements ' )
            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('invite_user')).is_displayed()

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('mail_box')).is_displayed()

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('editor_role')).is_displayed()

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('admin_role')).is_displayed()

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('viewer_role')).is_displayed()

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('select_region_box')).is_displayed()

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('cancel_button')).is_displayed()
            logger.info('all elements are visible there')

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            logger.error('An Exception occurred in test case verify content of user invite pop up 18')
            print(e)
            pytest.fail(e, pytrace=True)
