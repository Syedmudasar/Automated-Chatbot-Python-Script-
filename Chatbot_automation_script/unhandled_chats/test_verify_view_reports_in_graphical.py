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

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('open_drop_down1')).click()
            logger.info('User has dropped drop_down to select region type')

            element = HrBot_Config_mapper.hrbot_locators.get('philippines')

            Utility.move_to_target_element(element, driver)

            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('users'), 'visibility', driver)

            # validate that user is able to see current date conversation report

            # time.sleep(2)
            # conversation_count_number = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('conversation_counter1')).text
            # logger.info('Conversation number has been fetched from the home page', conversation_count_number)
            #
            # # time.sleep(2)
            # # driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('conversation_counter1')).click()
            # # logger.info('User has opened all conversation on current date')
            # #
            # # time.sleep(2)
            # # driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('download_icon')).is_displayed()
            # # logger.info('Download icon is visible there')
            #
            # # driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('download_icon')).click()
            # # logger.info('User has clicked on download button to download current report')
            # #
            # # driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('popup_close')).click()
            # # logger.info('User has closed the conversation reports popup')
            #
            # element = HrBot_Config_mapper.hrbot_locators.get('philippines')
            #
            # Utility.move_to_target_element(element, driver)
            #
            # Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('users'), 'visibility', driver)
            #
            # driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('')).is_displayed()
            # logger.info('Graphical reports is visible there')
            # # validate that user is able to download previous reports
            #
            # time.sleep(3)
            # driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('select_date_drop_box')).click()
            # logger.info('User has clicked on select date box')
            #
            # time.sleep(3)
            # driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('change_date_last_week')).click()
            # logger.info('User has changed the date as per last week')
            #
            # time.sleep(2)
            # driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('')).is_displayed()
            # logger.info('Graphical reports is visible there 1')
            #
            # # validate that user is able to see reports in graphical monthly
            #
            # time.sleep(2)
            # driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('select_date_drop_box')).click()
            # logger.info('User has clicked on select date box')
            #
            # time.sleep(3)
            # driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('change_date_last_month')).click()
            # logger.info('User has changed the date as per last week')
            #
            # time.sleep(2)
            # driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('')).is_displayed()
            # logger.info('Graphical reports is visible there 2')


        except Exception as e:
            allure.attach(driver.get_screenshots_as_png(), 'screenshots', AttachmentType.PNG)
            logger.error('An Exception occurred in test case verify reports display in graphical view 88')
            print(e)
            pytest.fail()