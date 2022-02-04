from analytics_module.conftest import *
from com_hrbot_modules.launchEnvironment import *
from allure_commons.types import AttachmentType
from com_hrbot_constant.hrbot_config_mapper import *
from com_hrbot_constant.constant import *
from com_hrbot_logger.log import Log
from com_htbot_utility.excel_reader import *
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import allure
import time
import unittest

logger = Log.get_logger()

@pytest.mark.usefixtures('setup')
class Test88(unittest.TestCase):

    def test88_verify_reports_in_graphical_view_previously_weekly_monthly(self):

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

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('analytics_report_module')).is_displayed()
            logger.info('Analytics and Reports module is visible in navigation bar at left side')

            open_drop_down1 = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('open_drop_down'))
            open_drop_down1.click()
            logger.info('User has dropped drop_down to select region type')

            time.sleep(3)
            elem = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('philippines'))
            print(elem.text)
            elem.click()

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('select_date_drop_box')).click()
            logger.info('User has clicked on date drop down to change date')

            time.sleep(3)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('change_date_last_month')).click()
            logger.info('User has selected last month')
            # time.sleep(3)
            # driver.execute_script("return arguments[0].scrollIntoView();", elem)
            # time.sleep(3)

            open_drop_down1 = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('open_drop_down1'))
            open_drop_down1.click()
            logger.info('User has dropped drop_down to select region type')

            time.sleep(3)
            elem = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('philippines'))
            print(elem.text)
            elem.click()

            time.sleep(3)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('select_date_drop_box1')).click()
            logger.info('User has clicked on date drop down to change date 1')

            time.sleep(5)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('change_date_last_month1')).click()
            logger.info('User has selected last month 1')

            time.sleep(3)

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('reports_graph')).is_displayed()
            logger.info('Reports is visible in graphical view')

        except Exception as e:
            allure.attach(driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            logger.error('An Exception occurred in test case verify reports display in graphical view 88')
            print(e)
            pytest.fail()