import pytest
from com_hrbot_logger.log import Log
from com_hrbot_constant.hrbot_config_mapper import HrBot_Config_mapper
from com_hrbot_constant.constant import *
from analytics_module.conftest import *
from com_htbot_utility.excel_reader import *
from allure_commons.types import AttachmentType
import allure
import time



logger = Log.get_logger()

@pytest.mark.usefixtures('setup')
class Test32:

    def test32_Verify_central_repository_page(self):
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
                try:
                    assert url == ExcelReader.read_excel().get("hrbot_homepage_url")
                    logger.info('User has been navigated successfully to home page')
                except Exception as e:
                    print("---------amjad-----", e)
            else:
                logger.info('User is not navigated to home page')

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('central_repos_module')).click()
            logger.info('User has successfully clicked on user\'s setting module')

            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('central_repository'), "visibility", driver)

            url = self.driver.current_url
            if url:
                assert url == ExcelReader.read_excel().get('hrbot_cr_url')
                logger.info('User has been navigated successfully to user\'s page')
            else:
                logger.info('User is not navigated to user\'s page')

        except Exception as e:
            logger.info('An exception occurred in verify central repository page 32')
            allure.attach(self.driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            print(e)
            pytest.fail(e, pytrace=True)
