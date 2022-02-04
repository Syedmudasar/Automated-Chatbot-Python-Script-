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
class Test53:

    # in order verify that if user does not enter template name to create template, gets error message
    # and click on save button test 49

    def test53_verify_user_allowed_add_delete_duplicate_videos_url_text_images(self):
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
            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('answers'), 'visibility', driver)

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('faq')).click()
            logger.info('User has clicked on successfully Faq repository')

            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('central_repository'), "visibility", driver)

            # click on new interaction button
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('new_interaction')).click()
            logger.info('User has clicked on new interaction button')


            flag = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('text')).is_displayed()
            assert flag == True
            logger.info('text is visible under answers tag')

            flag = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('url')).is_displayed()
            assert flag == True
            logger.info('url is visible under answers tag')

            flag = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('shuffle')).is_displayed()
            assert flag == True
            logger.info('shuffle is visible under answers tag')

            flag = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('image')).is_displayed()
            assert flag == True
            logger.info('image is visible under answers tag')

            flag = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('video')).is_displayed()
            assert flag == True
            logger.info('video is visible under answers tag')

            flag = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('carousel')).is_displayed()
            assert flag == True
            logger.info('carousel is visible under answers tag')
            # user has entered template name field
            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('template_input_box')).send_keys(
                ExcelReader.read_excel2().get('template_name1'))
            logger.info('User has entered successfully template name')


            time.sleep(4)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('question_input_box')).click()
            logger.info('User has clicked on successfully question text box')

            time.sleep(4)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('question_input_box')).send_keys(
                ExcelReader.read_excel2().get('question1'))
            logger.info('User has inserted question 1 into question box')

            time.sleep(4)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('carousel')).click()
            logger.info('User has clicked on carousel')

            time.sleep(4)
            try:
                driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('car_image')).click()
                element = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('car_image'))
                image = ExcelReader.read_excel1().get('image_path')
                print(image)
                try:
                    element.send_keys(image)
                    logger.info('User has uploaded a image')
                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)

            time.sleep(4)
            try:
                driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('carousel_video')).click()
            except Exception as e:
                print(e)
            time.sleep(3)
            try:
                element = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('carousel_video'))
                video = ExcelReader.read_excel1().get('video_path')
                print(video)
                element.send_keys(video)
                logger.info('User has uploaded a image')
            except Exception as e:
                print(e)

            time.sleep(4)
            element = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('carousal_description'))
            element.send_keys(ExcelReader.read_excel1().get('carousel_description'))
            logger.info('User has entered description')

            time.sleep(4)
            element = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('carousel_url'))
            element.send_keys(ExcelReader.read_excel1().get('carousel_url'))
            logger.info('User has entered url')

            time.sleep(4)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('duplicate1')).click()
            logger.info('User has created a duplicate carousel')

            time.sleep(4)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('delete2')).click()
            logger.info('User has deleted the duplicate carousel')

            time.sleep(2)

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('carousel_video')).click()
            logger.info('User has clicked inside video url')

            time.sleep(5)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('delete1')).click()
            logger.info('User has deleted last one carousel also')

            time.sleep(4)

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('carousel')).click()
            logger.info('User has clicked on carousel again')

            time.sleep(4)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('carousel_video')).click()
            logger.info('User has clicked inside video')

            time.sleep(4)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('copy1')).click()
            logger.info('User has copied the card')

            time.sleep(4)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('paste_card')).click()
            logger.info('User has pasted the card')

            time.sleep(4)
            flag = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('carousel_container2')).is_displayed()
            assert flag == True
            logger.info('The carousel container is visible')


        except Exception as e:
            allure.attach(driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            logger.error('An Exception occurred in test case verify user allowed text add delete and duplicate video under carousel tb 53')
            print(e)
            pytest.fail(e, pytrace=True)
