from analytics_module.conftest import *
from com_hrbot_constant.hrbot_config_mapper import HrBot_Config_mapper
from com_htbot_utility.excel_reader import *
import time
from com_hrbot_logger.log import Log
from allure_commons.types import AttachmentType
import allure


logger = Log.get_logger()

@pytest.mark.usefixtures("setup")
class Test4:

    def test4_Verify_Alert_Message_invalid_credetials(self):
        try:
            logger.info("Verify the Alert message while inserting invalid credentials to login page")
            logger.info("enter valid credentials to login page")

            try:
                self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_user_box")).send_keys(HrBot_Config_mapper.hrbot_config.get("invalid_user"))
                self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_pass_box")).send_keys(HrBot_Config_mapper.hrbot_config.get("invalid_password"))
                logger.info("The credentials are inserted successfully by user")
            except Exception as e:
                print(e)

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_button")).click()
            logger.info("user has successfully clicked on login button")

            time.sleep(2)

            logger.info("Validate Alert message is visible or not")
            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("error_message")).is_displayed()
            logger.info("Alter message is visible after entering invalid credentials")

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            logger.info("An Error occurred while verify ")
            print(e)
            pytest.fail(e, pytrace=True)


