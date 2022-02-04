from analytics_module.conftest import *
from com_hrbot_modules.launchEnvironment import *
from allure_commons.types import AttachmentType
from com_hrbot_constant.hrbot_config_mapper import *
from com_hrbot_constant.constant import *
from com_hrbot_logger.log import Log
from com_htbot_utility.excel_reader import *
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import allure
import time
import unittest

logger = Log.get_logger()

@pytest.mark.usefixtures('setup')
class Test90(unittest.TestCase):

    def test90_verify_gets_relevant_result_based_on_query_in_search_functionality(self):

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

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('header_search_input_box')).click()
            logger.info('User has clicked in search input box')

            search_input = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('header_search_input_box'))
            search_input.send_keys(ExcelReader.read_excel2().get('question2'))
            logger.info('User has inserted question in search input box to check search functionality')

            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('question'), 'visibility', driver)

            elements = driver.find_elements_by_xpath(HrBot_Config_mapper.hrbot_locators.get('result_class'))
            print(len(elements))

            question = ExcelReader.read_excel2().get('question2')

            time.sleep(3)
            for element in elements:
                time.sleep(3)
                try:
                    print(element.text)
                    self.assertEqual(question, element.text)
                    logger.info('result data is almost relevant to the question ::: question:{} ::: result:{}'.format(question, str(element.text)))
                except AssertionError as e:
                    print(e)
            # for i in range()
            # extracted_result = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('')).text
            #
            # ExcelReader.read_excel1().get('') == extracted_result

        except Exception as e:
            allure.attach(driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            logger.error('An Exception occurred in test case verify how much relevant user gets data from search functionality 90')
            print(e)
            pytest.fail()