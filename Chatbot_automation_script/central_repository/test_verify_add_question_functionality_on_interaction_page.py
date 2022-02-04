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
class Test137(unittest.TestCase):

    def test37_Verify_add_question_functionality_under_flow_repository(self):

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

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('enter_temp_name')).click()
            logger.info('User has clicked in temp name input box')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('enter_temp_name')).send_keys(ExcelReader.read_excel2().get('template_name'))
            logger.info('User has inserted temp name')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('ok_button')).click()
            logger.info('User has clocked on "OK" button')

            time.sleep(3)

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('add_button')).click()
            logger.info('User has clicked on plus icon to move to interaction page')

            time.sleep(3)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('question_input1')).is_displayed()
            logger.info('Add question input box is visible the 1')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('add_question')).click()
            logger.info('User has clicked on add button')

            time.sleep(1)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('question_input2')).is_displayed()
            logger.info('Add question input box is visible the 2')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('add_question')).click()
            logger.info('User has clicked on add button')

            time.sleep(1)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('question_input3')).is_displayed()
            logger.info('Add question input box is visible the 3')

        except Exception as e:
            logger.info('An exception occurred in verify add question functionality under flow repository 137')
            allure.attach(self.driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            print(e)
            pytest.fail(e, pytrace=True)
