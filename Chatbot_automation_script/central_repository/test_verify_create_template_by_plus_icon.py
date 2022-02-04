from com_htbot_utility.utility import Utility
from com_htbot_utility.excel_reader import ExcelReader
from com_hrbot_constant.hrbot_config_mapper import HrBot_Config_mapper
from com_hrbot_logger.log import Log
from analytics_module.conftest import *
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
import allure
import pytest
import time

logger = Log.get_logger()

# noinspection PyBroadException
@pytest.mark.usefixtures('setup')
class Test43:

    # to verify that template clickable in repository list or not

    def test43_verify_create_template_by_plus_icon(self):

        driver = self.driver

        try:
            logger.info('enter user\'s credentials to login page')
            element = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_user_box"))
            element.send_keys(HrBot_Config_mapper.hrbot_config.get("username"))

            element = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_pass_box"))
            element.send_keys(HrBot_Config_mapper.hrbot_config.get("password"))
            logger.info('User has successfully entered credentials')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_button")).click()
            logger.info('User has successfully clicked on login button')

            logger.info('Waiting for the element')
            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('central_repository_img'), 'visibility', driver)

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

            flag = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('faq_repository')).is_displayed()
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
            string = Utility.randomString(3)
            template_name = ExcelReader.read_excel2().get('template_name1')
            print(template_name+string)
            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('template_input_box')).send_keys(template_name + string)
            logger.info('User has entered successfully template name')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('question_input_box')).click()
            logger.info('User has clicked on successfully question text box')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('question_input_box')).send_keys(ExcelReader.read_excel2().get('question1'))
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
                driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('input')).send_keys(data)
                logger.info('User has entered answer in text input')
            except Exception as e:
                print(e)

            # create template click on save button
            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('save_button')).click()
            logger.info('User has successfully clicked on save button')

            # move to back to verify that new template is visible in list and click on back arrow button
            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('back_button')).click()

            # verify that visible or not
            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('template_list_title'), 'visibility', driver)

            elements = driver.find_elements_by_xpath(HrBot_Config_mapper.hrbot_locators.get('template_names'))
            ls = []
            for template in elements:
                ls.append(template.text)

            print(ls)
            if ExcelReader.read_excel2().get('template_name1') in ls:
                logger.info('The template exist in list')
            else:
                logger.info('The template does not exist')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('plus_icon')).click()
            logger.info('User has clicked on new interaction button')

            string = Utility.randomString(3)
            template_name = ExcelReader.read_excel2().get('template_name1')
            print(template_name + string)
            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('template_input_box')).send_keys(
                template_name + string)
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
                driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('input')).send_keys(data)
                logger.info('User has entered answer in text input')
            except Exception as e:
                print(e)

            # create template click on save button
            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('save_button')).click()
            logger.info('User has successfully clicked on save button')

            time.sleep(2)
            elements = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('template_save_message')).text
            assert elements == 'Template Saved Successfully'
            logger.info('template is created by plus icon')

        except Exception as e:
            allure.attach(driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            logger.error('An Exception occurred in test case verify create template by plus icon 43')
            print(e)
            pytest.fail(e, pytrace=True)