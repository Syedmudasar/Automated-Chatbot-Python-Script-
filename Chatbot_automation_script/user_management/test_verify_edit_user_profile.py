import pytest
from com_hrbot_logger.log import Log
from com_hrbot_constant.hrbot_config_mapper import HrBot_Config_mapper
from com_htbot_utility.excel_reader import *
import time
from allure_commons.types import AttachmentType
import allure
from analytics_module.conftest import *


logger = Log.get_logger()

@pytest.mark.usefixtures('setup')
class Test30:

    def test_edit_user_profile_link(self):
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

            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('user_management'), 'visibility', self.driver)

            before_update = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('individual_role')).text
            print(before_update)

            if before_update == 'viewer':
                time.sleep(2)
                self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('quick_action')).click()
                logger.info('User has successfully clicked on deactivate from action column in order to deactivate profile')

                time.sleep(1)
                self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('edit_profile')).click()
                logger.info('User has successfully clicked on edit to update profile')

                time.sleep(1)
                self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('editor_radio')).click()
                logger.info('User has changed role of user as viewer')

                time.sleep(1)
                self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('update_button')).click()
                logger.info('User has clicked on update user profile as editor')

            elif before_update == 'editor':
                time.sleep(2)
                self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('quick_action')).click()
                logger.info(
                    'User has successfully clicked on deactivate from action column in order to deactivate profile')

                time.sleep(1)
                self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('edit_profile')).click()
                logger.info('User has successfully clicked on edit to update profile')

                time.sleep(1)
                self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('viewer_radio')).click()
                logger.info('User has changed role of user as viewer')

                time.sleep(1)
                self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('update_button')).click()
                logger.info('User has clicked on update user profile as editor')

            time.sleep(3)
            after_update = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('individual_role')).text
            print(after_update)

            if before_update != after_update:
                logger.info('User role has been updated successfully')
            else:
                logger.info('edit functionality is not working')

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            logger.error('An Error occurred in verify edit_user_profile_link 30')
            print(e)
            pytest.fail(e, pytrace=True)

