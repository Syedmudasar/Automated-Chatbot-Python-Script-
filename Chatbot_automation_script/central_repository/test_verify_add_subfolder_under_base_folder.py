from com_hrbot_constant.hrbot_config_mapper import *
from com_htbot_utility.excel_reader import *
from com_hrbot_logger.log import Log
from com_htbot_utility.utility import *
from allure_commons.types import AttachmentType
from analytics_module.conftest import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import allure
import time

logger = Log.get_logger()


@pytest.mark.usefixtures('setup')
class Test70:

    # in order verify that if user does not enter template name to create template, gets error message
    # and click on save button test 49

    def test70_verify_add_sub_folder_under_base_folder_on_central_repository(self):
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

            time.sleep(3)
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
            time.sleep(4)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('faq')).click()
            logger.info('User has clicked on successfully Faq repository')

            # Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('central_repository'), "visibility", driver)

            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('template_list_title'), 'visibility', driver)

            flag = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('new_folder_button')).is_displayed()
            assert flag == True
            logger.info('New folder button is visible')

            time.sleep(4)
            folder_names = driver.find_elements_by_xpath(HrBot_Config_mapper.hrbot_locators.get('folder_names'))
            list_folder_names = []
            for name in folder_names:
                list_folder_names.append(name.text)

            print('Before creating new folder',list_folder_names)

            time.sleep(4)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('new_folder_button')).click()
            logger.info('User has clicked on add new folder')

            time.sleep(4)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('enter_folder_name')).send_keys(ExcelReader.read_excel2().get('folder_name'))
            logger.info('User has entered folder name as : ')

            time.sleep(4)
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

            # Utility.create_sub_folder(list_folder_names1, driver)

            time.sleep(3)
            counter = 0
            for names in list_folder_names1:
                counter += 1
                print(names)
                folder = ExcelReader.read_excel2().get('folder_name')
                if folder == names:
                    path = HrBot_Config_mapper.hrbot_locators.get('folder_path')

                    print("//*[text()='{}']".format(folder))
                    path = xpath.format(folder)
                    # xpath = "//span[text()='{}']".format(folder)
                    # print("//*[@class='rst__node'][{}]//div/div[2]//span[text()='New Folder']".format(counter))
                    # element1 = "//*[@class='rst__node'][{}]//div/div[2]//span[text()='New Folder']".format(counter)
                    # print(element1)
                    try:
                        time.sleep(2)
                        action = ActionChains(driver)
                        element = driver.find_element_by_xpath(path)
                        action.drag_and_drop_by_offset(element, 200, 0).perform()

                        time.sleep(4)
                        sub_folder
                        path1 = HrBot_Config_mapper.hrbot_locators.get('sub_folder')
                        x = path1.format(counter)
                        driver.find_element_by_xpath(x).click()
                        # action.move_to_element(element2).click(element2)
                        time.sleep(5)
                        break
                        # action..click_and_hold(element).move_by_offset(50, 0).release()
                        # x = "((//*[@class='rst__rowToolbar'])[{}]//div[@class='rst__rowNodeAdd'])/span[@class='text-btnTitle']".format(counter)
                        # print(x)
                        # time.sleep(2)
                        # action1 = ActionChains(driver)
                        # element2 = driver.find_element_by_xpath(x)
                        # action1.drag_and_drop(element, element2).perform()
                        #driver.find_element_by_xpath(x).click()
                    except Exception as e:
                        print('--------amjad------2', e)

            time.sleep(3)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('enter_folder_name')).send_keys(
                ExcelReader.read_excel2().get('sub_folder_name'))
            logger.info('User has entered sub folder name as : ')

            time.sleep(3)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('create_folder')).click()

            time.sleep(3)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('added_folder')).is_displayed()
            logger.info('Sub folder has been added')

        except Exception as e:
            allure.attach(driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            logger.error('An Exception occurred in test case verify add sub folder under base folder on central repository 70')
            print(e)
            pytest.fail(e, pytrace=True)
