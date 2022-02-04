import pytest
from com_hrbot_constant.hrbot_config_mapper import *
from com_htbot_utility.excel_reader import ExcelReader
from com_hrbot_logger.log import *
from analytics_module.conftest import *
from allure_commons.types import AttachmentType
import allure
import time

logger = Log.get_logger()

@pytest.mark.usefixtures('setup')
class Test38:

    def test38_verify_template_screen_content(self):
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

            url = self.driver.current_url
            if url:
                assert url == ExcelReader.read_excel().get('hrbot_cr_url')
                logger.info('User has been navigated successfully to user\'s page')
            else:
                logger.info('User is not navigated to user\'s page')

            time.sleep(2)
            try:
                self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('faq')).click()
                logger.info('User has clicked on FAQ repository')
            except Exception as e:
                print('-------amjad------', e)


            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('central_repository'), 'visibility', driver)

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

            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('back_button'), 'visibility', driver)

            url = self.driver.current_url
            if url:
                assert url == ExcelReader.read_excel().get('hrbot_edit_template_url')
                logger.info('User has been navigated to edit template page')
            else:
                logger.info('User has not been navigated to edit template page ')


            time.sleep(3)
            flag = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('template_input_box')).is_displayed()
            if flag:
                logger.info('Template input box is visible')
            else:
                logger.info('template name input box is not visible')

            flag = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('questions')).is_displayed()
            if flag:
                logger.info('Questions tag is visible there')
            else:
                logger.info('Questions tag is not visible there')

            flag = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('tags')).is_displayed()
            if flag:
                logger.info('Tags is visible there')
            else:
                logger.info('Tags is not visible there')

            flag = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('answers')).is_displayed()
            if flag:
                logger.info('Answers heading is visible there')
            else:
                logger.info('Answer heading is not visible there')

            flag = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('onesource')).is_displayed()
            if flag:
                logger.info('Onesource Link is visible there')
            else:
                logger.info('Onesource Link is not visible there')

            flag = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('text')).is_displayed()
            if flag:
                logger.info('Answer by text button is visible there')
            else:
                logger.info('Answer by text button is not visible there')

            flag = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('url')).is_displayed()
            if flag:
                logger.info('Answered by relevant Url button is visible')
            else:
                logger.info('Answered by relevant Url button is not visible')

            flag = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('shuffle')).is_displayed()
            if flag:
                logger.info('Answered by shuffle button is visible there')
            else:
                logger.info('Answered by shuffle button is not visible')

            flag = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('image')).is_displayed()
            if flag:
                logger.info('answered by Image button is visible there')
            else:
                logger.info('answered by Image button is not visible there')

            flag = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('carousel')).is_displayed()
            if flag:
                logger.info('Answered by carousel button is visible there')
            else:
                logger.info('Answered by carousel button is not visible there')

            flag = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('paste_card')).is_displayed()
            if flag:
                logger.info('paste card is visible')
            else:
                logger.info('paste card is visible')

            flag = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('save_button')).is_displayed()
            if flag:
                logger.info('Save button is visible ')
            else:
                logger.info('Save button is not visible  there')

            flag = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('revert_button')).is_displayed()
            if flag:
                logger.info('Revert button is visible there at right corner')
            else:
                logger.info('Revert button is not visible there at right corner')


        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            logger.error('An Error occurred in verify template screen content 38')
            print(e)
            pytest.fail(e, pytrace=True)