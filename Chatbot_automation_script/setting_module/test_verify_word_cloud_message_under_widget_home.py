from analytics_module.conftest import *
from com_hrbot_modules.launchEnvironment import *
from allure_commons.types import AttachmentType
from com_hrbot_constant.hrbot_config_mapper import *
from com_hrbot_constant.constant import *
from com_hrbot_logger.log import Log
from com_htbot_utility.excel_reader import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import allure
import time
import unittest

logger = Log.get_logger()

@pytest.mark.usefixtures('setup')
class Test128(unittest.TestCase):


    def test128_verify_word_cloud_message_under_widget_home_page(self):

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

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('setting_module1')).is_displayed()
            logger.info('Setting module is visible in navigation bar at left side')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('setting_module1')).click()
            logger.info('User has clicked on setting module')

            time.sleep(5)
            url = ExcelReader.read_excel().get('hrbot_setting_url')
            url1 = driver.current_url

            self.assertEqual(url, url1)
            logger.info('User has been navigated to setting page successfully')

            list_region = []
            region_elements = driver.find_elements_by_xpath(HrBot_Config_mapper.hrbot_locators.get('all_region'))
            for region in region_elements:
                list_region.append(region.text)
            logger.info('Region names have been fetched by script')

            list_region1 = ['TICA-El Salvador', 'TICA-Guatemala', 'TIC-Canada', 'TIE-Bulgaria', 'TIE-Ireland',
                             'TIE-Romania', 'TIE-United Kingdom', 'TII-India', 'TI-Philippines', 'TIUS-USA']

            self.assertEqual(list_region, list_region1)
            logger.info('Region names displayed under setting module')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('region_bulgaria')).click()
            logger.info('User has selected bulgaria region type')

            flag = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('widget_homepage')).is_enabled()
            if flag:
                logger.info('widget homepage settings is clickable')

            time.sleep(3)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('widget_homepage')).click()
            logger.info('User has clicked on widget homepage button')

            time.sleep(3)
            flag = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('save_button')).is_displayed()
            if flag:
                logger.info('Save button is clickable')
            else:
                logger.info('Save button is not clickable there')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('upload_image')).send_keys(ExcelReader.read_excel1().get('xavient_logo'))
            logger.info('User has uploaded a image to widget homepage')

            time.sleep(3)
            flag = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('save_button')).is_displayed()
            if flag:
                logger.info('Image has been uploaded successfully as well as save button become clickable')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('feedback_message')).click()
            logger.info('User has clicked in word cloud message input box')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('feedback_message')).send_keys(ExcelReader.read_excel1().get('word_cloud_message'))
            logger.info('User has inserted word cloud message into input box')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('save_button'))
            logger.info('User has saved the widget homepage')

            time.sleep(2)

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('saved_additional_setting')).is_displayed()
            logger.info('The widget home saved successfully')

        except Exception as e:
            allure.attach(driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            logger.error('An Exception occurred in test case verify word cloud message under widget homepage 128')
            print(e)
            pytest.fail()