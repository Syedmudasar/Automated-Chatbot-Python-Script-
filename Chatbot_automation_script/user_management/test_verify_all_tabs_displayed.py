from analytics_module.conftest import *
from com_htbot_utility.excel_reader import *
import unittest
from com_htbot_utility.utility import *
from com_hrbot_constant.hrbot_config_mapper import *
from allure_commons.types import AttachmentType

import allure
import time


logger = Log.get_logger()

@pytest.mark.usefixtures("setup")
class Test13(unittest.TestCase):

    flag = False

    def test13_validate_all_tabs_displayed(self):
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
            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('conversation_reports'), 'visibility', self.driver)

            url = self.driver.current_url
            if url:
                assert url == ExcelReader.read_excel().get("hrbot_homepage_url")
                logger.info('User has been navigated successfully to home page')
            else:
                logger.info('User is not navigated to home page')

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('users_setting')).click()
            logger.info('User has successfully clicked on user\'s  module')

            url = self.driver.current_url
            url1 = ExcelReader.read_excel().get('hrbot_users_url')
            if url:
                assert url == url1.replace('\n', '')
                logger.info('User has been successfully to user\'s page')
            else:
                logger.info('User is not navigated to user\'s page')

            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('user_management'), 'visibility', self.driver)

            logger.info('validate all tabs are visible or not')

            flag = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('activate_tab')).is_displayed()
            self.assertEqual(flag, True, 'Activate tab is not visible')

            flag = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('deactivate_tab')).is_displayed()
            self.assertEqual(flag, True, 'Deactivate tab is not visible')

            flag = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('invited_tab')).is_displayed()
            self.assertEqual(flag, True, 'Invited tab is not visible')

            flag = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('total_users')).is_displayed()
            self.assertEqual(flag, True, 'Total users tab is not visible there')
            logger.info('All tabs are visible there')

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            logger.error('An Error occurred in verify all tabs')
            print(e)
            pytest.fail(e, pytrace=True)