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
class Test75(unittest.TestCase):

    def test75_verify_select_item_under_drop_down_in_unhandled_message(self):

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
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('open_drop_down')).click()
            logger.info('User has dropped drop_down box for select region')

            time.sleep(3)
            flag = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('drop_down')).is_displayed()
            self.assertEqual(flag, True)
            logger.info('Drop down is visible there')

            number = Utility.random_number()
            path = HrBot_Config_mapper.hrbot_locators.get('select_region_drop')
            print(path)
            xpath = path.format(number)

            driver.find_element_by_xpath(xpath).click()
            logger.info('User has selected a item from drop down list')

            time.sleep(4)


        except Exception as e:
            allure.attach(driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            logger.info('An Exception occurred in test case verify unhandled message 75')
            print(e)
            pytest.fail()
