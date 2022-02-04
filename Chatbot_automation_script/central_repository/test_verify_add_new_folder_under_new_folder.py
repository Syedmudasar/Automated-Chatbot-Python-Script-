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
class Test69:

    # in order verify that if user does not enter template name to create template, gets error message
    # and click on save button test 49

    def test69_verify_add_new_folder_under_add_new_folder_button_on_central_repository(self):
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

            flag = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('new_folder_button')).is_displayed()
            assert flag == True
            logger.info('New folder button is visible')

            folder_names = driver.find_elements_by_xpath(HrBot_Config_mapper.hrbot_locators.get('folder_names'))
            list_folder_names = []
            for name in folder_names:
                list_folder_names.append(name.text)

            print('Before creating new folder',list_folder_names)

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('new_folder_button')).click()
            logger.info('User has clicked on add new folder')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('enter_folder_name')).send_keys(ExcelReader.read_excel2().get('folder_name'))
            logger.info('User has entered folder name as ::: {}'.format(ExcelReader.read_excel2().get('folder_name')))

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('create_folder')).click()
            logger.info('User has created new folder successfully')

            time.sleep(3)

            folder_names1 = driver.find_elements_by_xpath(HrBot_Config_mapper.hrbot_locators.get('folder_names'))
            list_folder_names1 = []
            for name1 in folder_names1:
                list_folder_names1.append(name1.text)

            print('After adding new folder :', list_folder_names1)

            if ExcelReader.read_excel2().get('folder_name') in list_folder_names1:
                logger.info('The folder name exist means new folder created successfully')
            else:
                logger.info('The folder name does not exist means new folder not created unfortunately')

        except Exception as e:
            allure.attach(driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            logger.error('An Exception occurred in test case verify add new folder under new folder button on central repository 69')
            print(e)
            pytest.fail(e, pytrace=True)
