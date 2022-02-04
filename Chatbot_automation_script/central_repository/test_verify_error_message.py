import pytest
from com_hrbot_logger.log import *
from com_hrbot_constant.hrbot_config_mapper import *
from analytics_module.conftest import *
import allure
from allure_commons.types import AttachmentType
from com_htbot_utility.excel_reader import *

logger = Log.get_logger()

@pytest.mark.usefixtures('setup')
class Test39:

    def test_Verify_user_gets_an_error_message_blank_template_name(self):
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

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('central_repos_module')).click()
            logger.info('User has successfully clicked on user\'s central_repository')

            url = self.driver.current_url
            if url:
                assert url == ExcelReader.read_excel().get('hrbot_cr_url')
                logger.info('User has been navigated successfully to user\'s page')
            else:
                logger.info('User is not navigated to user\'s page')

            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('central_repository1'), 'visibility', driver)

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('faq')).click()
            logger.info('User has clicked on FAQ repository')

            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('central_repository1'), 'visibility', driver)
            url = self.driver.current_url
            if url:
                assert url == ExcelReader.read_excel().get("hrbot_faq_url")
                logger.info('User has been navigated successfully to faq repository interaction page')
            else:
                logger.info('User is not navigated to faq repository interaction page')

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), 'screenshots', type=AttachmentType.PNG)
            logger.error('Exception in test_Verify_user_gets_an_error_message_blank_template_name 39')
            print(e)
            pytest.fail(e, pytrace=True)
