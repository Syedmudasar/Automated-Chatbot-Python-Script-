from com_hrbot_modules.launchEnvironment import *
from analytics_module.conftest import *
from allure_commons.types import AttachmentType
from com_hrbot_logger.log import Log
import allure
import pytest
import time

logger = Log.get_logger()

@pytest.mark.usefixtures('setup')
class Test7:

    # Validate The password is visible or after click on show link

    # noinspection PyBroadException
    def test7_validate_password_visibility(self):

        try:
            logger.info('Enter user credentials to login\'s input box')
            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_user_box")).send_keys(HrBot_Config_mapper.hrbot_config.get("username"))
            time.sleep(3)
            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_pass_box")).send_keys(HrBot_Config_mapper.hrbot_config.get("password"))
            logger.info('User has successfully entered credentials to login page')

            # validate the password before clicking on show password ling
            # and after clicking on that if type got change it's working fine

            # validate before clicking on the link

            logger.info("Validate type of password before clicking on the link")
            element = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("show_password"))
            before_value = element.get_attribute('title')
            print(before_value)

            logger.info('Now user needs to click on show password link to validate')
            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("show_password_eye")).click()
            logger.info("User has successfully clicked on show password link")

            # after clicking on the link
            time.sleep(5)

            logger.info("Validate type of password after clicking on the link")
            element = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("show_password"))
            after_value = element.get_attribute('title')
            print(after_value)

            if before_value != after_value:
                logger.info('Password show link is working as expected')
            else:
                logger.error('Password not being converted from text to visible password as expected ')

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            logger.error('An Error occurred in verify password show link')
            print(e)
            pytest.fail(e, pytrace=True)