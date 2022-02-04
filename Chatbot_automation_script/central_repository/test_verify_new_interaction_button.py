import pytest
from com_hrbot_logger.log import Log
from com_hrbot_constant.hrbot_config_mapper import HrBot_Config_mapper
import time
from analytics_module.conftest import *
from com_htbot_utility.excel_reader import *
import allure
from allure_commons.types import AttachmentType

logger = Log.get_logger()


@pytest.mark.usefixtures('setup')
class Test36:

    def test36_Verify_new_interaction_button(self):
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

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('central_repository')).click()
            logger.info('User has successfully clicked on user\'s central_repository')

            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('central_repository1'), 'visibility', driver)
            url = self.driver.current_url

            if url:
                assert url == ExcelReader.read_excel().get('hrbot_cr_url')
                logger.info('User has been navigated successfully to user\'s page')
            else:
                logger.info('User is not navigated to user\'s page')

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('faq_repository')).click()
            logger.info('User has clicked on FAQ repository')


            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('central_repository1'), 'visibility', driver)

            url = self.driver.current_url
            if url:
                assert url == ExcelReader.read_excel().get("hrbot_faq_url")
                logger.info('User has been navigated successfully to faq repository interaction page')
            else:
                logger.info('User is not navigated to faq repository interaction page')

            flag = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('new_interaction')).is_displayed()
            if flag:
                logger.info('New interaction button is visible there')
            else:
                logger.info('New interaction button is not visible there')

            flag = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('new_interaction')).is_enabled()
            if flag:
                logger.info('New interaction button is clickable')
            else:
                logger.info('New interaction is not clickable')

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), 'screenshots', type=AttachmentType.PNG)
            logger.error('An Error occurred in verify new interaction button 36')
            print(e)
            pytest.fail(e, pytrace=True)
