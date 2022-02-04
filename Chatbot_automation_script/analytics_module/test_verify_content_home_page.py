from analytics_module.conftest import *
from com_hrbot_modules.launchEnvironment import *
from allure_commons.types import AttachmentType
import allure
import time
import unittest
logger = Log.get_logger()

@pytest.mark.usefixtures("setup")
class Test5(unittest.TestCase):

    def test5_verify_content_home_page(self):
        try:
            # Utility.explicit_Wait(HrBot_Config_mapper.hrbot_locators.get('logo'), self.driver)

            logger.info('enter user\'s credentials to login page')
            element = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_user_box"))
            element.send_keys(HrBot_Config_mapper.hrbot_config.get("username"))

            element = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_pass_box"))
            element.send_keys(HrBot_Config_mapper.hrbot_config.get("password"))
            logger.info('User has successfully entered credentials')

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('login_button')).click()
            logger.info('User has clicked on login button successfully')

            driver = self.driver
            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('conversation'), 'visibility', driver)
            logger.info('Validate the home page content start from header')

            flag = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("logo")).is_displayed()
            assert flag == True
            logger.info('Telus Logo is visible on left corner')

            logger.info("Validate the user name who is logged in,  is visible or not , at right corner ")
            flag = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("logged_user")).is_displayed()
            assert flag == True
            logger.info("User name is Visible there")

            logger.info('Validate the Search input box is visible at right corner or not')
            flag = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("header_search_input_box")).is_displayed()
            assert flag == True
            logger.info('The search input bos is visible there')

            # Validate the Conversation header

            logger.info('Validate the conversation header on home page')
            flag = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("conversation_reports")).is_displayed()

            assert flag == True
            logger.info('The Conversation heading is visible as Conversation reports')

            logger.info('Validate the select region and drop down on conversation header')
            flag = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("select_region")).is_displayed()
            assert flag == True

            flag = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("select_region_drop_box")).is_displayed()
            assert flag == True
            logger.info('The Select region is visible there')

            logger.info('Validate the select date option and date drop down')
            flag = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("select_date")).is_displayed()
            assert flag == True
            logger.info('Select date is visible')

            flag = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("select_date_drop_box")).is_displayed()
            assert flag == True
            logger.info('The date option is visible as well as drop down')

            # Validate the conversation report container

            logger.info('Validate The conversation Report detail like users and conversation etc')
            flag = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("users")).is_displayed()
            assert flag == True
            logger.info('Users tag is visible there')

            flag = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("conversation")).is_displayed()
            assert flag == True
            logger.info('Conversation tag is visible there')

            time.sleep(2)
            try:
                element = HrBot_Config_mapper.hrbot_locators.get("unhandled")
                print(element)
                flag = self.driver.find_element_by_xpath(element).is_displayed()
                assert flag == True
                logger.info('Unhandled Inquiries Tag is visible there')
            except Exception as e:
                print('------amjad-------', e)

            time.sleep(2)
            flag = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("users_sentiments")).is_displayed()
            assert flag == True
            logger.info('Users sentiments Tag is visible there')
            logger.info('All information accurately are visible there in conversation box')

            # Validate interaction report chart in at the bottom side of home page

            logger.info('Validate the Interaction report heading is there or not ')
            flag = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("interaction_report")).is_displayed()
            if flag:
                logger.info("Interaction Report heading is visible there")
            else:
                logger.info('Interaction Report heading is not visible there')

            logger.info('Validate the interaction report is visible or not')
            flag = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("interaction_report_chart")).is_displayed()
            assert flag == True
            logger.info('Interaction report chart is visible there')

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            logger.info('An Error occurred in verify home page content Test case')
            print('Exception name is :', e)
            pytest.fail(e, pytrace=True)