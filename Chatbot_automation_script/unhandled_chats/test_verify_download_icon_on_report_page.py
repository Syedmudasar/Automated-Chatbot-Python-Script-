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
class Test86(unittest.TestCase):

    def test86_verify_download_icon_on_conversation_reports_page(self):

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

            element = HrBot_Config_mapper.hrbot_locators.get('philippines')

            Utility.move_to_target_element(element, driver)

            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('users'), 'visibility', driver)

            # validate that user is able to see current date conversation report

            time.sleep(2)
            conversation_count_number = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('conversation_counter1')).text
            logger.info('Conversation number has been fetched from the home page', conversation_count_number)

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('conversation_counter1')).click()
            logger.info('User has opened all conversation on current date')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('download_icon')).is_displayed()
            logger.info('Download icon is visible there')

            time.sleep(4)
        except Exception as e:
            allure.attach(driver.get_screenshots_as_png(), 'screenshots', AttachmentType.PNG)
            logger.error('An Exception occurred in test case verify download icon 86')
            print(e)
            pytest.fail()