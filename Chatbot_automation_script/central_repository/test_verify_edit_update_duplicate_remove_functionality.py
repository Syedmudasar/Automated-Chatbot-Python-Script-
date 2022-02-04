from com_htbot_utility.utility import Utility
from com_htbot_utility.excel_reader import ExcelReader
from com_hrbot_constant.hrbot_config_mapper import HrBot_Config_mapper
from com_hrbot_logger.log import Log
from analytics_module.conftest import *
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure
import pytest
import time

logger = Log.get_logger()

# noinspection PyBroadException
@pytest.mark.usefixtures('setup')
class Test47:

    # to verify that edit, update, duplicate, and remove template

    def test47_verify_edit_update_duplicate_remove_template(self):

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

            time.sleep(2)
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
            string = Utility.randomString(2)
            template_name = ExcelReader.read_excel2().get('template_name1')
            template = template_name+string
            print(template)

            time.sleep(2)
            element1 = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('template_input_box'))
            element1.send_keys(template_name + string)
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


            # verify that visible or not

            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('template_editable'), 'visibility', driver)

            template_name = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('template_editable')).text
            logger.info('before edit template name it is template name')

            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('edit_profile'), 'visibility', driver)

            # from hare verify edit button functionality and update, duplicate, remove

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('edit_profile')).click()
            logger.info('User has successfully clicked on edit_profile button')

            # try:
            #     element1.send_keys(Keys.RETURN)
            #     time.sleep(4)
            #     element1.clear()
            #     logger.info('User has successfully cleared template name to edit name')
            # except Exception as e:
            #     print(e)

            string = Utility.randomString(2)
            template_name = ExcelReader.read_excel2().get('template_name1')
            print(template_name + string)
            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('template_input_box')).send_keys(template_name)
            logger.info('User has entered successfully template name')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('save_button')).click()
            logger.info('User has successfully clicked on save button1')

            time.sleep(2)
            template_name1 = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('template_editable')).text
            print(template_name1)
            logger.info('after edit template name it is template name')

            assert template_name1 != template_name
            logger.info('template name is edited successfully')

            time.sleep(2)
            flag = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('update_bot')).is_enabled()
            print(flag)

            assert flag == True
            logger.info('update button is disabled')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('duplicate_bot')).click()
            logger.info('User has clicked on duplicate button in order to create duplicate temp')

            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('duplicate_done'), 'visibility', driver)

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('duplicate_done')).click()
            logger.info('User has clicked on done button')

            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('remove_bot'), 'visibility', driver)

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('remove_bot')).click()
            logger.info('User has clicked on remove button')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('delete_template')).click()
            logger.info('User has clicked delete button on confirmation pup up')

            # verify that visible or not
            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('template_list_title'), 'visibility', driver)

            elements = driver.find_elements_by_xpath(HrBot_Config_mapper.hrbot_locators.get('template_names'))
            ls = []
            for template in elements:
                ls.append(template.text)

            print(ls)
            if template_name1 in ls:
                logger.info('The template exist in list')
            else:
                logger.info('The template does not exist')


        except Exception as e:
            allure.attach(driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            logger.error('An Exception occurred in test case verify edit update duplicate, remove template 47')
            print(e)
            pytest.fail(e, pytrace=True)