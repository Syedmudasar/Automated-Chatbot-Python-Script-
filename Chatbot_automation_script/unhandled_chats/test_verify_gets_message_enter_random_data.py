from com_hrbot_constant.hrbot_config_mapper import *
from com_hrbot_logger.log import Log
from com_hrbot_constant.hrbot_config_mapper import *
from com_htbot_utility.excel_reader import *
from allure_commons.types import AttachmentType
from analytics_module.conftest import *
import allure
import unittest
import pytest
import random

logger = Log.get_logger()


# noinspection PyBroadException
@pytest.mark.usefixtures('setup')
class Test79(unittest.TestCase):

    def test79_verify_gets_message_enter_random_data_into_search_text_field(self):

        driver = self.driver

        try:
            url = driver.current_url
            url1 = ExcelReader.read_excel().get('login_page_url')
            self.assertEqual(url, url1, 'Both are equal')
            logger.info('User is navigated to login page successfully')

            logger.info('enter user\'s credentials to login page')
            element = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_user_box"))
            element.send_keys(HrBot_Config_mapper.hrbot_config.get("username"))

            element = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_pass_box"))
            element.send_keys(HrBot_Config_mapper.hrbot_config.get("password"))
            logger.info('User has successfully entered credentials')

            time.sleep(5)

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_button")).click()
            logger.info('User has successfully clicked on login button')

            logger.info('Waiting for the element')
            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('conversation_reports'), 'visibility', driver)

            url = driver.current_url
            url1 = ExcelReader.read_excel().get('hrbot_homepage_url')
            print(url1, url)

            self.assertEqual(url, url1, 'Both are equal')
            logger.info('User ia navigated to home page successfully')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('unhandled_chat')).is_displayed()
            logger.info('Unhandled module is visible in navigation bar at left side')

            time.sleep(3)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('unhandled_chat')).click()
            logger.info('User has clicked on unhandled message module')

            time.sleep(3)
            for i in range(10):
                flag = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('list_unhandled_message')).is_displayed()
                if flag:
                    break
                else:
                    driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('')).click()

                    number = Utility.random_number()
                    path = HrBot_Config_mapper.hrbot_locators.get('select_region_drop')
                    print(path)
                    xpath = path.format(number)

                    driver.find_element_by_xpath(xpath).click()
                    logger.info('User has selected a item from drop down list')

                    time.sleep(4)

            if flag:
                    time.sleep(3)
                    driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('check_box1')).click()
                    logger.info('User has checked the check box to delete unhandled records')

                    driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('quick_action')).click()
                    logger.info('User has clicked on quick action')

                    driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('assign_button')).click()
                    logger.info('User has clicked on assign option from drop_down')

                    time.sleep(3)
                    driver.find_element_by_xpath(
                        HrBot_Config_mapper.hrbot_locators.get('assign_interaction')).is_displayed()
                    logger.info('Assign template is visible after clicking on assign option')

                    driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('on_assign_temp_drop_down')).click()
                    logger.info('User has clicked on drop_down to choose repository FAQ')

                    driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('on_assign_temp_faq')).click()
                    logger.info('User has changed repository FAQ from drop_down ')

                    driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('search_database_input')).click()
                    logger.info('User has clicked in search input box')

                    driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('search_database_input')).send_keys(HrBot_Config_mapper.hrbot_config.get(''))
                    logger.info('User has inserted data into search input field')

                    driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('message_enter_random_data')).is_displayed()
                    logger.info('User gets a message after entering random data')
            else:
                logger.info('There is not unhandled message')

        except Exception as e:
            allure.attach(driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            logger.info('An Exception occurred in test case verify user gets a message enter random data into text field 79')
            print(e)
            pytest.fail()
