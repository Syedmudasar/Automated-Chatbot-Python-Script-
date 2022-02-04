from com_hrbot_modules.launchEnvironment import LaunchEnvironment
from analytics_module.conftest import *
from com_hrbot_constant.constant import Constant
from allure_commons.types import AttachmentType
import allure


logger = Log.get_logger()

@pytest.mark.usefixtures("setup")
class Test6:

    # noinspection PyBroadException
    def test6_validate_alert_message_with_blank_credential(self):

        # Validate the Alert message without entering login credential
        try:
            logger.info('Validate the Alert message in case without entering credentials ')
            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_button")).click()
            logger.info("User has clicked successfully on login button")

            logger.info('Waiting for until element to be visible')
            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get("error_message"), 'visibility', self.driver)

            logger.info('Validate the alert message  below of the input box')
            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("enter_mail")).is_displayed()
            logger.info('Alert message is visible there')

            logger.info('Validate the alert message  below of the input box')
            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("enter_password")).is_displayed()
            logger.info('Alert message is visible there')

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            logger.error('An Error occurred in verify alert message with blank credential')
            print(e)
            pytest.fail(e, pytrace=True)

