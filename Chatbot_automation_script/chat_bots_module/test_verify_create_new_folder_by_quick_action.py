from analytics_module.conftest import *
from com_hrbot_modules.launchEnvironment import *
from allure_commons.types import AttachmentType
from com_hrbot_constant.hrbot_config_mapper import *
from com_hrbot_constant.constant import *
from com_hrbot_logger.log import Log
from com_htbot_utility.excel_reader import *
from selenium.webdriver.common.action_chains import ActionChains
import allure
import time
import unittest

logger = Log.get_logger()

@pytest.mark.usefixtures('setup')
class Test102(unittest.TestCase):


    def test102_verify_add_new_folder_under_quick_action_on_chat_bots_page(self):

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

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('chat_bots')).is_displayed()
            logger.info('Chat bots module is visible in navigation bar at left side')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('chat_bots')).click()
            logger.info('User has clicked on chat bots module')

            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('chat_bots_heading'), 'visibility', driver)

            url = ExcelReader.read_excel().get('hrbot_chat_bots_url')
            url1 = driver.current_url

            self.assertEqual(url1, url)
            logger.info('User has navigated successfully to chat bots page')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('chat_bots_heading')).is_displayed()
            logger.info('Chat bots is visible on chat bots page')

            all_region_elements = driver.find_elements_by_xpath(HrBot_Config_mapper.hrbot_locators.get('all_region_type'))

            region_extracted = []

            list_region_type = ['Small Talk', 'TICA-El Salvador', 'TICA-Guatemala', 'TIC-Canada', 'TIE-Bulgaria', 'TIE-Ireland',
             'TIE-Romania', 'TIE-United Kingdom', 'TII-India', 'TI-Philippines', 'TIUS-USA']

            for region in all_region_elements:
                region_extracted.append(region.text)

            print(region_extracted)

            self.assertEqual(region_extracted, list_region_type)
            logger.info('As expected all region type are visible perfectly ::: {}'.format(region_extracted))

            region_number = Utility.random_number(len(region_extracted))

            path = HrBot_Config_mapper.hrbot_locators.get('select_region2')

            region_name = driver.find_element_by_xpath(path.format(region_number)).text
            driver.find_element_by_xpath(path.format(region_number)).click()
            logger.info('User has clicked on region ::: {}'.format(region_name))

            time.sleep(5)
            Utility.verify_urls(self, region_name, driver)

            folder_names = driver.find_elements_by_xpath(HrBot_Config_mapper.hrbot_locators.get('folder_names'))
            list_folder_names = []
            for name in folder_names:
                list_folder_names.append(name.text)

            print('Before creating new folder', list_folder_names)

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('new_folder_button')).click()
            logger.info('User has clicked on add new folder')

            time.sleep(3)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('enter_folder_name')).send_keys(ExcelReader.read_excel2().get('folder_name'))
            logger.info('User has entered folder name as :::{} '.format(ExcelReader.read_excel2().get('folder_name')))

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('create_folder')).click()
            logger.info('User has created new folder successfully')

            time.sleep(3)

            folder_names1 = driver.find_elements_by_xpath(HrBot_Config_mapper.hrbot_locators.get('folder_names'))
            list_folder_names1 = []
            for name1 in folder_names1:
                list_folder_names1.append(name1.text)

            print('After adding new folder :', list_folder_names1)

            if ExcelReader.read_excel2().get('folder_name') in list_folder_names1:
                logger.info('The folder name exist means new folder created successfully')
            else:
                logger.info('The folder name does not exist means new folder not created unfortunately')

            time.sleep(3)
            counter = 0
            for names in list_folder_names1:
                counter += 1
                print(names)
                folder = ExcelReader.read_excel2().get('folder_name')
                if folder == names:
                    path = HrBot_Config_mapper.hrbot_locators.get('folder_path')
                    path1 = path.format(folder)
                    try:
                        time.sleep(2)
                        action = ActionChains(driver)
                        element = driver.find_element_by_xpath(path1)
                        action.drag_and_drop_by_offset(element, 200, 0).perform()

                        time.sleep(4)
                        path2 = HrBot_Config_mapper.hrbot_locators.get('sub_folder')
                        x = path2.format(counter)
                        driver.find_element_by_xpath(x).click()
                        time.sleep(5)
                        break
                    except Exception as e:
                        print('--------xxx trip apple xxx------2', e)

            time.sleep(3)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('enter_folder_name')).send_keys(
                ExcelReader.read_excel2().get('sub_folder_name'))
            logger.info('User has entered sub folder name as ::: '.format(ExcelReader.read_excel2().get('sub_folder_name')))

            time.sleep(3)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('create_folder')).click()

            time.sleep(3)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('added_folder')).is_displayed()
            logger.info('Sub folder has been added')


        except Exception as e:
            allure.attach(driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            logger.error('An Exception occurred in test case verify create new folder under quick action 102')
            print(e)
            pytest.fail()