import pytest
from com_hrbot_constant.hrbot_config_mapper import *
from com_htbot_utility.excel_reader import ExcelReader
from com_hrbot_logger.log import *
from analytics_module.conftest import *
import allure
from allure_commons.types import AttachmentType

logger = Log.get_logger()

@pytest.mark.usefixtures('setup')
class Test37:

    def test37_verify_template_screen(self):
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

            time.sleep(3)
            url = self.driver.current_url
            if url:
                assert url == ExcelReader.read_excel().get('hrbot_cr_url')
                logger.info('User has been navigated successfully to central repository\'s page')
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

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('new_interaction')).click()
            logger.info('New interaction button is clicked by user')

            time.sleep(3)
            url = self.driver.current_url
            if url:
                try:
                    assert url == ExcelReader.read_excel().get('hrbot_edit_template_url')
                    logger.info('User has been navigated to edit template page')
                except Exception as e:
                    print('eeeeeeee', e)
            else:
                logger.info('User has not been navigated to edit template page ')

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            logger.error('An Error occurred in verify template screen 37')
            print(e)
            pytest.fail(e, pytrace=True)
