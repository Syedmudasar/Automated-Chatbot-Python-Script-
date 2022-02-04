import pytest
from com_hrbot_logger.log import Log
from com_hrbot_constant.hrbot_config_mapper import HrBot_Config_mapper
from com_htbot_utility.excel_reader import *
import allure
from allure_commons.types import AttachmentType
from analytics_module.conftest import *


logger = Log.get_logger()

@pytest.mark.usefixtures('setup')
class Test16:

    def test16_Verify_activate_profile_functionality_under_Deactivated_tab(self):
        try:
            logger.info('enter user\'s credentials to login page')
            element = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_user_box"))
            element.send_keys(HrBot_Config_mapper.hrbot_config.get("username"))

            element = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_pass_box"))
            element.send_keys(HrBot_Config_mapper.hrbot_config.get("password"))
            logger.info('User has successfully entered credentials')

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_button")).click()
            logger.info('User has successfully clicked on login button')

            driver = self.driver
            logger.info('Waiting for the element')
            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('conversation_reports'), 'visibility', driver)

            url = self.driver.current_url
            if url:
                assert url == ExcelReader.read_excel().get("hrbot_homepage_url")
                logger.info('User has been navigated successfully to home page')
            else:
                logger.info('User is not navigated to home page')

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('users_management')).click()
            logger.info('User has successfully clicked on user\'s setting module')

            url = self.driver.current_url
            url1 = ExcelReader.read_excel().get('hrbot_users_url')
            print(url, url1)
            if url:
                assert url == url1.replace('\n', '')
                logger.info('User has been navigated successfully to user\'s page')
            else:
                logger.info('User is not navigated to user\'s page')

            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('user_management'), 'visibility', driver)

            deactivate_numbers = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('deactivate_users_num')).text
            print(deactivate_numbers)

            i = 0
            while i < 2:
                if int(deactivate_numbers) > 0:

                    self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('deactivate_tab')).click()
                    logger.info('User has successfully clicked on deactivated tab from tab list')

                    time.sleep(4)
                    self.driver.find_element_by_xpath(
                        HrBot_Config_mapper.hrbot_locators.get('quick_deactivation')).click()
                    logger.info('User has successfully clicked on action')

                else:
                    # self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('activate_tab')).click()
                    # logger.info('User has successfully clicked on action')

                    time.sleep(2)
                    self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('quick_action')).click()
                    logger.info('User has clicked on quick action')

                    self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('deactivate')).click()
                    logger.info('User has clicked on deactivate option')

                    self.driver.find_element_by_xpath(
                        HrBot_Config_mapper.hrbot_locators.get('confirmation_button')).click()
                    logger.info('User has clicked on yes button')

                    time.sleep(3)
                    deactivate_numbers = self.driver.find_element_by_xpath(
                        HrBot_Config_mapper.hrbot_locators.get('deactivate_users_num')).text
                    logger.info('Deactivated user number has been fetched successfully')
                    print(deactivate_numbers)
                i += 1

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            logger.error('An Error occurred in verify activate profile again under deactivate functionality')
            print(e)
            pytest.fail(e, pytrace=True)
