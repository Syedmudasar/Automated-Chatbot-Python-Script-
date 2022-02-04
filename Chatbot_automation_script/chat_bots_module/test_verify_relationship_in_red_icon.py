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
class Test110(unittest.TestCase):

    # invoke multiple time this test case
    
    for i in range(3):
        def test110_verify_relationship_in_red_icon(self):

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

                all_region_elements = driver.find_elements_by_xpath(
                    HrBot_Config_mapper.hrbot_locators.get('all_region_type'))

                region_extracted = []

                list_region_type = ['Small Talk', 'TICA-El Salvador', 'TICA-Guatemala', 'TIC-Canada', 'TIE-Bulgaria',
                                    'TIE-Ireland',
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

                if region_name in ['Small Talk', 'TICA-El Salvador', 'TIC-Canada', 'TIE-Ireland', 'TIE-Romania', 'TI-Philippines', 'TIUS-USA']:
                    Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('open_drop_down2'), 'visibility', driver)

                    driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('open_drop_down2')).click()
                    logger.info('User has dropped drop_down------')

                    time.sleep(2)
                    driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('drop_down')).is_displayed()
                    logger.info('Drop_down is visible under chat bots------')

                    region_number = Utility.random_number(8)
                    xpath = HrBot_Config_mapper.hrbot_locators.get('random_region')
                    region_type = Utility.choose_random_region1(region_number, xpath, driver)
                else:
                    Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('open_drop_down1'), 'visibility',
                                           driver)

                    driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('open_drop_down1')).click()
                    logger.info('User has dropped drop_down ++++++++++')

                    time.sleep(2)
                    driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('drop_down')).is_displayed()
                    logger.info('Drop_down is visible under chat bots ++++++++')

                    region_number = Utility.random_number(8)
                    xpath = HrBot_Config_mapper.hrbot_locators.get('random_region')
                    region_type = Utility.choose_random_region1(region_number, xpath, driver)

                for i in range(5):
                    if region_type in ['Small Talk', 'TICA-El Salvador', 'TIC-Canada', 'TIE-Ireland', 'TIE-Romania', 'TI-Philippines', 'TIUS-USA']:
                        time.sleep(4)
                        driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('open_drop_down2')).click()
                        logger.info('User has dropped drop_down 1')

                        time.sleep(2)
                        driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('drop_down')).is_displayed()
                        logger.info('Drop_down is visible under chat bots 1')

                        region_number = Utility.random_number(8)
                        xpath = HrBot_Config_mapper.hrbot_locators.get('random_region')
                        region_type1 = Utility.choose_random_region1(region_number, xpath, driver)
                        print(region_type1)
                        region_type = region_type1

                        Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('relationship_red_icon'), 'visibility', driver)

                        flag = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('relationship_red_icon')).is_displayed()
                        if flag:
                            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('relationship_red_icon')).click()
                            break
                    else:
                        time.sleep(4)
                        driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('open_drop_down1')).click()
                        logger.info('User has dropped drop_down 2')

                        time.sleep(2)
                        driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('drop_down')).is_displayed()
                        logger.info('Drop_down is visible under chat bots 2')

                        region_number = Utility.random_number(8)
                        xpath = HrBot_Config_mapper.hrbot_locators.get('random_region')
                        region_type = Utility.choose_random_region1(region_number, xpath, driver)
                        print(region_type)

                        # Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('relationship_red_icon'), 'visibility', driver)
                        time.sleep(4)
                        flag = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('relationship_red_icon')).is_displayed()

                        if flag:
                            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('relationship_red_icon')).click()
                            time.sleep(10)
                            break

            except Exception as e:
                allure.attach(driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
                logger.error('An Exception occurred in test case verify relationship in red icon 110')
                print(e)
                pytest.fail()