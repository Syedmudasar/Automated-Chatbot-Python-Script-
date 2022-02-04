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
class Test46:

    # to verify that all elements are visible under answers tag

    def test46_verify_all_elements_under_answers_tag(self):

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

            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('answers'), 'visibility', driver)

            flag = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('text')).is_displayed()
            assert flag == True
            logger.info('Text button is visible')

            flag = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('url')).is_displayed()
            assert flag == True
            logger.info('URL button is visible')

            flag = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('shuffle')).is_displayed()
            assert flag == True
            logger.info('Shuffle tag is visible')

            flag = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('image')).is_displayed()
            assert flag == True
            logger.info('Image button is visible')

            flag = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('video')).is_displayed()
            assert flag == True
            logger.info('Video button is visible')

            flag = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('carousel')).is_displayed()
            assert flag == True
            logger.info('Carousel button is visible')


        except Exception as e:
            allure.attach(driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            logger.error('An Exception occurred in test case verify all elements under answers tag 46')
            print(e)
            pytest.fail(e, pytrace=True)