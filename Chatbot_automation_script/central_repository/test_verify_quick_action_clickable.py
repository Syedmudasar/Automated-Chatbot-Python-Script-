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
class Test62:

    # in order verify that if user does not enter template name to create template, gets error message
    # and click on save button test 49

    def test62_verify_quick_action_icon_clickable_on_central_repository(self):
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

            # Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('central_repository'), "visibility", driver)

            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('template_list_title'), 'visibility', driver)

            flag = driver.find_element_by_xpath(
                HrBot_Config_mapper.hrbot_locators.get('quick_action_icon')).is_displayed()
            assert flag == True
            logger.info('Quick action is visible')

            flag = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('quick_action_icon')).is_enabled()
            assert flag == True
            logger.info('Quick action icon is clickable')


            # elements = driver.find_elements_by_xpath(HrBot_Config_mapper.hrbot_locators.get('template_names'))
            # ls = []
            # for template in elements:
            #     ls.append(template.text)
            #
            # print('Before remove a template : ', ls)
            # # click on new interaction button
            # driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('check_mark')).click()
            # logger.info('User has checked on check mark button')
            #
            #
            # time.sleep(3)
            # flag = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('remove_button')).is_displayed()
            # assert flag == True
            # logger.info('Remove button is visible means user is able to see remove button once user checks the check box')
            #
            # driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('remove_button')).click()
            # logger.info('User has removed the template from tem list')
            #
            # flag = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('confirmation_pop')).is_displayed()
            # assert flag == True
            # logger.info('Confirmation window is popped up when user pressed remove button')
            #
            # driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('')).click()
            # logger.info('User has clicked on delete button')
            #
            # Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('template_list_title'), 'visibility', driver)
            #
            # elements = driver.find_elements_by_xpath(HrBot_Config_mapper.hrbot_locators.get('template_names'))
            # ls1 = []
            # for template in elements:
            #     ls1.append(template.text)
            #
            # print('After remove the template : ', ls1)
            #
            # assert ls != ls1
            # logger.info('Both template list are different so the template removed successfully')


        except Exception as e:
            allure.attach(driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            logger.error('An Exception occurred in test case verify quick action is clickable icon on central repository 62')
            print(e)
            pytest.fail(e, pytrace=True)
