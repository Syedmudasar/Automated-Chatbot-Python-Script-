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
class Test85(unittest.TestCase):

    def test85_verify_reports_current_date_yesterday_last_week_month(self):

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

            conversation_count_number = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('conversation_counter1')).text
            logger.info('Conversation number has been fetched from the home page', conversation_count_number)

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('conversation_counter1')).click()
            logger.info('User has opened all conversation on current date')

            session_ides = driver.find_elements_by_xpath(HrBot_Config_mapper.hrbot_locators.get('conversation_session_id'))
            list_session_id = []
            for ids in session_ides:
                list_session_id.append(ids.text)


            self.assertEqual(conversation_count_number, len(list_session_id))
            logger.info('Both are equal conversation number and conversation session ides')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('popup_close')).click()
            logger.info('User has closed the conversation reports popup 1')
            # number = Utility.random_number()
            # path = HrBot_Config_mapper.hrbot_locators.get('select_region_drop')
            # print(path)
            # xpath = path.format(number)
            #
            # driver.find_element_by_xpath(xpath).click()
            # logger.info('User has selected a item from drop down list')

            # validate that user is also able to see yesterday's report

            time.sleep(4)
            current_date = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('select_date_drop_box')).text
            print('before change date : ', current_date)



            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('select_date_drop_box')).click()
            logger.info('User has clicked on select date box')

            time.sleep(3)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('change_date_yesterday')).click()
            logger.info('User has changed the date as per yesterday')

            time.sleep(3)
            back_date = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('select_date_drop_box')).text
            print('After change date : ', back_date)

            time.sleep(3)
            self.assertNotEqual(current_date, back_date)
            logger.info('User has changed the date successfully')

            conversation_count_number1 = driver.find_element_by_xpath(
                HrBot_Config_mapper.hrbot_locators.get('conversation_counter1')).text
            logger.info('Conversation number has been fetched from the home page', conversation_count_number1)

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('conversation_counter1')).click()
            logger.info('User has opened all conversation on current date')

            session_ides = driver.find_elements_by_xpath(
                HrBot_Config_mapper.hrbot_locators.get('conversation_session_id'))
            list_session_id1 = []
            for ids in session_ides:
                list_session_id.append1(ids.text)

            self.assertEqual(conversation_count_number1, len(list_session_id1))
            logger.info('Both are equal conversation number and conversation session ides')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('popup_close')).click()
            logger.info('User has closed the conversation reports popup 2')

            # validate that user is able to see last week reports

            time.sleep(4)
            current_date = driver.find_element_by_xpath(
                HrBot_Config_mapper.hrbot_locators.get('select_date_drop_box')).text
            print('before change date : ', current_date)

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('select_date_drop_box')).click()
            logger.info('User has clicked on select date box')

            time.sleep(3)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('change_date_last_week')).click()
            logger.info('User has changed the date as per last week')

            time.sleep(3)
            back_date = driver.find_element_by_xpath(
                HrBot_Config_mapper.hrbot_locators.get('select_date_drop_box')).text
            print('After change date : ', back_date)

            time.sleep(3)
            self.assertNotEqual(current_date, back_date)
            logger.info('User has changed the date successfully')

            conversation_count_number1 = driver.find_element_by_xpath(
                HrBot_Config_mapper.hrbot_locators.get('conversation_counter1')).text
            logger.info('Conversation number has been fetched from the home page', conversation_count_number1)

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('conversation_counter1')).click()
            logger.info('User has opened all conversation on current date')

            session_ides = driver.find_elements_by_xpath(
                HrBot_Config_mapper.hrbot_locators.get('conversation_session_id'))
            list_session_id1 = []
            for ids in session_ides:
                list_session_id.append1(ids.text)

            self.assertEqual(conversation_count_number1, len(list_session_id1))
            logger.info('Both are equal conversation number and conversation session ides')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('popup_close')).click()
            logger.info('User has closed the conversation reports popup 3')

            # validate that user also is able to see month reports

            time.sleep(4)
            current_date = driver.find_element_by_xpath(
                HrBot_Config_mapper.hrbot_locators.get('select_date_drop_box')).text
            print('before change date : ', current_date)

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('select_date_drop_box')).click()
            logger.info('User has clicked on select date box')

            time.sleep(3)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('change_date_last_month')).click()
            logger.info('User has changed the date as per last week')

            time.sleep(3)
            back_date = driver.find_element_by_xpath(
                HrBot_Config_mapper.hrbot_locators.get('select_date_drop_box')).text
            print('After change date : ', back_date)

            time.sleep(3)
            self.assertNotEqual(current_date, back_date)
            logger.info('User has changed the date successfully')

            conversation_count_number1 = driver.find_element_by_xpath(
                HrBot_Config_mapper.hrbot_locators.get('conversation_counter1')).text
            logger.info('Conversation number has been fetched from the home page', conversation_count_number1)

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('conversation_counter1')).click()
            logger.info('User has opened all conversation on current date')

            session_ides = driver.find_elements_by_xpath(
                HrBot_Config_mapper.hrbot_locators.get('conversation_session_id'))
            list_session_id1 = []
            for ids in session_ides:
                list_session_id.append1(ids.text)

            self.assertEqual(conversation_count_number1, len(list_session_id1))
            logger.info('Both are equal conversation number and conversation session ides')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('popup_close')).click()
            logger.info('User has closed the conversation reports popup 3')

            time.sleep(4)


        except Exception as e:
            allure.attach(driver.get_screenshots_as_png(), 'screenshots', AttachmentType.PNG)
            logger.error('An Exception occurred in test case verify reports yesterday last week and month 85')
            print(e)
            pytest.fail()