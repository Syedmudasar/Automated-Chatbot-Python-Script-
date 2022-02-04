from com_hrbot_constant.hrbot_config_mapper import *
from com_htbot_utility.excel_reader import *
from com_hrbot_logger.log import Log
from com_htbot_utility.utility import *
from allure_commons.types import AttachmentType
from analytics_module.conftest import *
from selenium.webdriver.common.keys import Keys
import pytest
import allure
import time


logger = Log.get_logger()

@pytest.mark.usefixtures('setup')
class Test54:

    # in order verify that if user does not enter template name to create template, gets error message
    # and click on save button test 49

    def test54_verify_user_allowed_check_checkBox(self):
        try:
            driver = self.driver

            logger.info('enter user\'s credentials to login page')
            element = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_user_box"))
            element.send_keys(HrBot_Config_mapper.hrbot_config.get("username"))

            element = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_pass_box"))
            element.send_keys(HrBot_Config_mapper.hrbot_config.get("password"))
            logger.info('User has successfully entered credentials')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_button")).click()
            logger.info('User has successfully clicked on login button')

            logger.info('Waiting for the element')
            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('conversation_reports'), 'visibility', driver)

            url = driver.current_url
            url1 = ExcelReader.read_excel().get("hrbot_homepage_url")
            print(url1, url)
            if url:
                try:
                    assert url == url1.replace('\n', '')
                    logger.info('User has been navigated successfully to home page')
                except Exception as e:
                    print("---------amjad-----", e)
            else:
                logger.info('User is not navigated to home page')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('central_repository_img')).click()
            logger.info('User has successfully clicked on user\'s module')

            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('central_repository'), "visibility", driver)

            url = driver.current_url
            url1 = ExcelReader.read_excel().get('hrbot_cr_url')
            if url:
                assert url == url1.replace('\n', '')
                logger.info('User has been navigated successfully to user\'s page')
            else:
                logger.info('User is not navigated to user\'s page')

            flag = driver.find_element_by_xpath(
                HrBot_Config_mapper.hrbot_locators.get('faq_repository')).is_displayed()
            if flag:
                logger.info('FAQ is visible there')
            else:
                logger.info('FAQ is not visible')

            # click on faq repository

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('faq')).click()
            logger.info('User has clicked on successfully Faq repository')

            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('central_repository'), "visibility", driver)

            # click on new interaction button
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('new_interaction')).click()
            logger.info('User has clicked on new interaction button')

            # user has entered template name field
            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('template_input_box')).send_keys(
                ExcelReader.read_excel2().get('template_name1'))
            logger.info('User has entered successfully template name')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('question_input_box')).click()
            logger.info('User has clicked on successfully question text box')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('question_input_box')).send_keys(
                ExcelReader.read_excel2().get('question1'))
            logger.info('User has inserted question 1 into question box')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('text_answer')).click()
            logger.info('User has clicked on text button')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('text_input_box')).click()
            logger.info('user has clicked on input box')

            # enter answer card to the text field
            time.sleep(2)
            data = ExcelReader.read_excel1().get('text_answer')
            print(data)
            try:
                text_input = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('input'))
                text_input.send_keys(data)
                logger.info('User has entered answer in text input')
            except Exception as e:
                print(e)

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('check_box')).click()
            logger.info('User is able to check the check box')


        except Exception as e:
            allure.attach(driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            logger.error('An Exception occurred in test case verify user allowed check the check box 54')
            print(e)
            pytest.fail(e, pytrace=True)
