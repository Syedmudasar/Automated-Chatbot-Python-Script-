import pytest
from com_hrbot_logger.log import Log
from com_hrbot_constant.hrbot_config_mapper import HrBot_Config_mapper
from analytics_module.conftest import *
from com_hrbot_constant.constant import *
from com_htbot_utility.excel_reader import *
from allure_commons.types import AttachmentType
import allure
import time
import unittest


logger = Log.get_logger()


@pytest.mark.usefixtures('setup')
class Test135(unittest.TestCase):

    def test35_Verify_enter_temp_name_pop_after_click_on_new_interaction_button(self):

        driver = self.driver

        try:
            logger.info('enter user\'s credentials to login page')
            element = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_user_box"))
            element.send_keys(HrBot_Config_mapper.hrbot_config.get("username"))

            element = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_pass_box"))
            element.send_keys(HrBot_Config_mapper.hrbot_config.get("password"))
            logger.info('User has successfully entered credentials')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_button")).click()
            logger.info('User has successfully clicked on login button')

            logger.info('Waiting for the element')
            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('conversation_reports'), 'visibility', driver)

            url = driver.current_url
            if url:
                assert url == ExcelReader.read_excel().get("hrbot_homepage_url")
                logger.info('User has been navigated successfully to home page')
            else:
                logger.info('User is not navigated to home page')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('central_repos_module')).click()
            logger.info('User has successfully clicked on user\'s setting module')

            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('central_repository'), 'visibility', driver)

            url = driver.current_url
            if url:
                assert url == ExcelReader.read_excel().get('hrbot_cr_url')
                logger.info('User has been navigated successfully to user\'s page')
            else:
                logger.info('User is not navigated to user\'s page')

            time.sleep(2)
            flag = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('flow')).is_displayed()
            if flag:
                logger.info('FLOW Repository is visible there')
            else:
                logger.info('FLOW is not visible there')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('flow')).click()
            logger.info('User has clicked on flow repository')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('new_interaction')).is_displayed()
            logger.info('New interaction button is visible there')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('new_interaction')).click()
            logger.info('User has clicked on new interaction button')

            time.sleep(2)
            flag = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('enter_temp_name_pop')).is_displayed()
            self.assertEqual(flag, True)
            logger.info('Enter temp name pop is visible')

        except Exception as e:
            logger.info('An exception occurred in verify enter temp name pop after click on new interaction button under flow repository 135')
            allure.attach(self.driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            print(e)
            pytest.fail(e, pytrace=True)
