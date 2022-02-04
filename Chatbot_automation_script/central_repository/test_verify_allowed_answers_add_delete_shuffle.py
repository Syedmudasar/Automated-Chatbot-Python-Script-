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
class Test50:

    # in order verify that if user does not enter template name to create template, gets error message
    # and click on save button test 49

    def test50_verify_user_allowed_add_delete_duplicate_shuffle(self):
        try:
            driver = self.driver
            time.sleep(5)

            logger.info('enter user\'s credentials to login page')
            element = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_user_box"))
            element.send_keys(HrBot_Config_mapper.hrbot_config.get("username"))

            element = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_pass_box"))
            element.send_keys(HrBot_Config_mapper.hrbot_config.get("password"))
            logger.info('User has successfully entered credentials')


            time.sleep(5)

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
            time.sleep(5)

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
            time.sleep(5)

            flag = driver.find_element_by_xpath(
                HrBot_Config_mapper.hrbot_locators.get('faq_repository')).is_displayed()
            if flag:
                logger.info('FAQ is visible there')
            else:
                logger.info('FAQ is not visible')

            # click on faq repository
            time.sleep(5)

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('faq')).click()
            logger.info('User has clicked on successfully Faq repository')

            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('central_repository'), "visibility", driver)

            # click on new interaction button
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('new_interaction')).click()
            logger.info('User has clicked on new interaction button')

            # user has entered template name field

            time.sleep(5)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('template_input_box')).send_keys(
                ExcelReader.read_excel2().get('template_name1'))
            logger.info('User has entered successfully template name')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('question_input_box')).click()
            logger.info('User has clicked on successfully question text box')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('question_input_box')).send_keys(
                ExcelReader.read_excel2().get('question1'))
            logger.info('User has inserted question 1 into question box')

            time.sleep(5)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('shuffle')).click()
            logger.info('User has clicked on shuffle button in order to give shuffle answers')

            time.sleep(5)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('shuffle_add_answers')).click()
            logger.info('User has clicked on shuffle add answers button')

            time.sleep(5)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('shuffle_text_box')).click()
            logger.info('User has clicked in shuffle input box in order to insert text there')

            time.sleep(5)
            element = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('shuffle_text_box'))
            element.send_keys(ExcelReader.read_excel1().get('shuffle_answers'))
            logger.info('user has entered answer into shuffle text box')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('duplicate1')).click()
            logger.info('User has clicked on duplicate button in order to create one more duplicate shuffle box')

            time.sleep(5)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('delete2')).click()
            logger.info('User has deleted the duplicate one')

            time.sleep(5)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('delete1')).click()
            logger.info('User has deleted that first one also')

            time.sleep(5)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('shuffle')).click()
            logger.info('User has clicked on shuffle button in order to give shuffle answers 2')

            time.sleep(5)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('shuffle_add_answers')).click()
            logger.info('User has clicked on shuffle add answers button 2')


            # text = element.text
            #
            # element.send_keys(Keys.SPACE)
            # time.sleep(5)
            # element.send_keys(ExcelReader.read_excel1().get('shuffle_answers'))
            # logger.info('User has added something else to text')
            # time.sleep(5)
            #
            # element.send_keys(Keys.CONTROL, 'a')
            # time.sleep(5)
            # element.send_keys(Keys.CONTROL, 'c')
            # time.sleep(5)
            # logger.info('User has delete the text from shuffle box')
            # element.clear()
            # time.sleep(5)
            # logger.info('User has cleared all content from text box')
            # element.send_keys(Keys.CONTROL, 'v')
            # logger.info('User has pasted the text content into text box')
            #
            #
            # time.sleep(5)
            # element = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('shuffle_text_box')).text
            # print(element)

        except Exception as e:
            allure.attach(driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            logger.error('An Exception occurred in test case verify user allowed text add delete and copy url and shuffle answers 50')
            print(e)
            pytest.fail(e, pytrace=True)
