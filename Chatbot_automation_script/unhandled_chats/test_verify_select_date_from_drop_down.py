from analytics_module.conftest import *
from com_hrbot_modules.launchEnvironment import *
from allure_commons.types import AttachmentType
from com_hrbot_constant.hrbot_config_mapper import *
from com_hrbot_constant.constant import *
from com_hrbot_logger.log import Log
import allure
import time
import unittest

logger = Log.get_logger()

pytest.mark.usefixtures('setup')
class Test84(unittest.TestCase):

    def test84_verify_select_date_from_drop_down(self):

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

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('region_drop_down')).click()
            logger.info('User has dropped drop_down to select region type')

            number = Utility.random_number()
            path = HrBot_Config_mapper.hrbot_locators.get('select_region_drop')
            print(path)
            xpath = path.format(number)

            driver.find_element_by_xpath(xpath).click()
            logger.info('User has selected a item from drop down list')

            time.sleep(4)

            # region_text = driver.find_element_by_xpath(xpath).text


        except Exception as e:
            allure.attach(driver.get_screenshots_as_png(), 'screenshots', AttachmentType.PNG)
            logger.error('An Exception occurred in test case verify select date from drop down 84')
            print(e)
            pytest.fail()