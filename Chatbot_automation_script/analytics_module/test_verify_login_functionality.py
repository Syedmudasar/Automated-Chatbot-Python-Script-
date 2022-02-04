from com_htbot_utility.excel_reader import *
from analytics_module.conftest import *
from com_hrbot_logger.log import Log
from com_hrbot_constant.hrbot_config_mapper import HrBot_Config_mapper
from com_htbot_utility.utility import *
from allure_commons.types import AttachmentType
import allure
import pytest
import time

logger = Log.get_logger()

@pytest.mark.usefixtures("setup")
class Test3:

    def test3_Verify_HomePage_with_Valid_credentials(self):
        try:
            time.sleep(5)

            logger.info("Enter valid user credential in input box")
            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_user_box")).send_keys(HrBot_Config_mapper.hrbot_config.get("username"))
            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_pass_box")).send_keys(HrBot_Config_mapper.hrbot_config.get("password"))
            logger.info("Login credentials are entered successfully ")

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_button")).click()
            logger.info('User has clicked successfully on login button')

            logger.info("Wait until to be loaded the home page")
            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get("conversation_reports"), 'visibility', self.driver)
            logger.info("Home page is loaded successfully")

            print('current url is loading..........')
            url = self.driver.current_url
            if url:
                assert url == ExcelReader.read_excel().get("hrbot_homepage_url")
                logger.info('user is navigated successfully on home page')
            else:
                logger.error('not exact match')

        except Exception as e:
            allure(self.driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            logger.error("An Error occurred while verify login functionality 3")
            print(e)
            pytest.fail(e, pytrace=True)