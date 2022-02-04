import pytest
from com_hrbot_logger.log import Log
from com_hrbot_constant.hrbot_config_mapper import HrBot_Config_mapper
from analytics_module.conftest import *
from com_hrbot_constant.constant import *
from com_htbot_utility.excel_reader import *
from allure_commons.types import AttachmentType
import allure
import time
import unittest


logger = Log.get_logger()


@pytest.mark.usefixtures('setup')
class Test150(unittest.TestCase):

    def test150_Verify_save_functionality_on_interaction_page(self):

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
            if url:
                assert url == ExcelReader.read_excel().get("hrbot_homepage_url")
                logger.info('User has been navigated successfully to home page')
            else:
                logger.info('User is not navigated to home page')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('central_repos_module')).click()
            logger.info('User has successfully clicked on user\'s setting module')

            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('central_repository'), 'visibility', driver)

            url = driver.current_url
            if url:
                assert url == ExcelReader.read_excel().get('hrbot_cr_url')
                logger.info('User has been navigated successfully to user\'s page')
            else:
                logger.info('User is not navigated to user\'s page')

            time.sleep(2)
            flag = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('flow')).is_displayed()
            if flag:
                logger.info('FLOW Repository is visible there')
            else:
                logger.info('FLOW is not visible there')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('flow')).click()
            logger.info('User has clicked on flow repository')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('new_interaction')).is_displayed()
            logger.info('New interaction button is visible there')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('new_interaction')).click()
            logger.info('User has clicked on new interaction button')

            time.sleep(2)
            flag = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('enter_temp_name_pop')).is_displayed()
            self.assertEqual(flag, True)
            logger.info('Enter temp name pop is visible')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('enter_temp_name')).click()
            logger.info('User has clicked in temp name input box')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('enter_temp_name')).send_keys(ExcelReader.read_excel2().get('template_name'))
            logger.info('User has inserted temp name')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('ok_button')).click()
            logger.info('User has clocked on "OK" button')

            time.sleep(3)

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('add_button')).click()
            logger.info('User has clicked on plus icon to move to interaction page')

            time.sleep(2)

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('template_input_box')).click()
            logger.info('User has clicked in enter tamp name input box')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('template_input_box')).send_keys(ExcelReader.read_excel1().get('template_title'))
            logger.info('User has entered template title as :::{}'.format(ExcelReader.read_excel1().get('template_title')))

            time.sleep(3)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('question_input1')).is_displayed()
            logger.info('Add question input box is visible the 1')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('question_input1')).click()
            logger.info('User has clicked in question input box 1')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('question_input1')).send_keys(
                ExcelReader.read_excel2().get('question2'))
            logger.info('User has added one question to the template')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('add_question')).click()
            logger.info('User has clicked on add button')

            time.sleep(1)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('question_input2')).is_displayed()
            logger.info('Add question input box is visible the 2')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('question_input2')).click()
            logger.info('User has clicked in question input box 2')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('question_input2')).send_keys(
                ExcelReader.read_excel2().get('question5'))
            logger.info('User has added one question to the template')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('add_question')).click()
            logger.info('User has clicked on add button')

            time.sleep(1)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('question_input3')).is_displayed()
            logger.info('Add question input box is visible the 3')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('question_input3'))
            logger.info('User has clicked in question input box 3')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('question_input3')).send_keys(
                ExcelReader.read_excel2().get('question6'))
            logger.info('User has added one question to the template')

            # validate add answer more than two
            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('text')).click()
            logger.info('User has clicked on text under answer tag')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('text_input_box')).click()
            logger.info('User has clicked in input box under answer 1')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('text_input_box')).send_keys(
                ExcelReader.read_excel1().get('answer1'))
            logger.info('User has inserted first answer 1')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('text')).click()
            logger.info('User has clicked on text under answer tag 1')

            time.sleep(4)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('text_input_box')).click()
            logger.info('User has clicked in input box under answer')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('text_input_box')).send_keys(
                ExcelReader.read_excel1().get('answer2'))
            logger.info('User has inserted second answer')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('text')).click()
            logger.info('User has clicked on text under answer tag')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('text_input_box')).click()
            logger.info('User has clicked in input box under answer')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('text_input_box')).send_keys(
                ExcelReader.read_excel1().get('answer3'))
            logger.info('User has inserted third answer')

            # validate url by giving answer by url under answer tag
            time.sleep(3)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('url')).click()
            logger.info('User has clicked on url under answer tag 1')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('url_input')).click()
            logger.info('User has clicked in url input box 1')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('url_input')).send_keys(
                ExcelReader.read_excel1().get('answer_by_url1'))
            logger.info('User has inserted url into url input box 1')

            time.sleep(3)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('url')).click()
            logger.info('User has clicked on url under answer tag 2')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('url_input1')).click()
            logger.info('User has clicked in url input box 2')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('url_input1')).send_keys(
                ExcelReader.read_excel1().get('answer_by_url2'))
            logger.info('User has inserted url into url input box 2')

            # validate shuffle answer by this under answer tag

            time.sleep(3)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('shuffle')).click()
            logger.info('User has clicked on shuffle under answer tag 1')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('shuffle_add_answers')).click()
            logger.info('User has clicked on add answer button 1')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('shuffle_text_box')).click()
            logger.info('User has clicked in input box 1')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('shuffle_text_box')).send_keys(ExcelReader.read_excel1().get('answer_by_shuffle1'))
            logger.info('User has inserted shuffle answer 1')

            time.sleep(3)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('shuffle')).click()
            logger.info('User has clicked on shuffle under answer tag 2')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('shuffle_add_answers1')).click()
            logger.info('User has clicked on add answer button 2')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('shuffle_text_box1')).click()
            logger.info('User has clicked in input box 2')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('shuffle_text_box1')).send_keys(
                ExcelReader.read_excel1().get('answer_by_shuffle2'))
            logger.info('User has inserted shuffle answer 2')

            time.sleep(3)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('shuffle')).click()
            logger.info('User has clicked on shuffle under answer tag 3')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('shuffle_add_answers2')).click()
            logger.info('User has clicked on add answer button 3')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('shuffle_text_box2')).click()
            logger.info('User has clicked in input box 3')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('shuffle_text_box2')).send_keys(
                ExcelReader.read_excel1().get('answer_by_shuffle3'))
            logger.info('User has inserted shuffle answer 3')

            time.sleep(3)

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('image')).click()
            logger.info('User has clicked on image tag under answer tag 1')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('upload_image')).send_keys(ExcelReader.read_excel1().get('answer_by_image1'))
            logger.info('User has uploaded a image about hr 1')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('image')).click()
            logger.info('User has clicked on image tag  under answer 2')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('upload_image1')).send_keys(
                ExcelReader.read_excel1().get('answer_by_image2'))
            logger.info('User has uploaded a image about hr')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('image')).click()
            logger.info('User has clicked on image tag  under answer 3')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('upload_image2')).send_keys(
                ExcelReader.read_excel1().get('answer_by_image3'))
            logger.info('User has uploaded a image about hr 3')

            time.sleep(3)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('video')).click()
            logger.info('User has clicked on video tag under answer')

            time.sleep(3)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('enter_video_url')).click()
            logger.info('User has clicked in video input')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('enter_video_url')).send_keys(ExcelReader.read_excel1().get('answer_by_video1'))
            logger.info('User has entered video url to upload')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('upload_video4')).click()
            logger.info('User has clicked on done button to upload video')

            time.sleep(3)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('video')).click()
            logger.info('User has clicked on video tag under answer')

            time.sleep(3)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('enter_video_url1')).click()
            logger.info('User has clicked in video input')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('enter_video_url1')).send_keys(
                ExcelReader.read_excel1().get('answer_by_video2'))
            logger.info('User has entered video url to upload')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('upload_video5')).click()
            logger.info('User has clicked on done button to upload video')

            time.sleep(3)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('carousel')).click()
            logger.info('User has clicked on carousel under answer')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('add_image_url')).click()
            logger.info('User has clicked in add image url input box')

            time.sleep(3)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('add_image_url')).send_keys(ExcelReader.read_excel1().get('answer_by_image1'))
            logger.info('User has entered image url 1')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('carousel_video')).click()
            logger.info('User has clicked in add video url input')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('carousel_video')).send_keys(ExcelReader.read_excel1().get('answer_by_video1'))
            logger.info('User has entered video url')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('carousal_description')).click()
            logger.info('User has clicked in carousel description')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('carousal_description')).send_keys(ExcelReader.read_excel1().get('hr_description'))
            logger.info('User has entered HR description')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('carousel_url')).click()
            logger.info('User has clicked in carousel url')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('carousel_url')).send_keys(ExcelReader.read_excel1().get('answer_by_url1'))
            logger.info('User has inserted a url')

            time.sleep(5)

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('quick_reply')).click()
            logger.info('User has clicked on quick reply under answer tag')

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('quick_reply_input_box1')).click()
            logger.info('User has clicked in quick reply input box')

            time.sleep(5)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('quick_reply_input_box1')).send_keys(ExcelReader.read_excel1().get('answer_by_quick_reply'))
            logger.info('User has insert quick reply answer into quick reply')

            element = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('add_title_name'))
            print(type(element))
            path = HrBot_Config_mapper.hrbot_locators.get('add_title_name')
            Utility.explicit_Wait1(path, 'visibility', driver)

            time.sleep(2)
            try:
                driver.execute_script("arguments[0].click();", element)
                logger.info('User has clicked on add title hare button to add title in quick reply 1')
            except Exception as e:
                print(e)

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('enter_title_name')).click()
            logger.info('User has clicked in title input box 1')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('enter_title_name')).send_keys(ExcelReader.read_excel1().get('title_name_under_quick'))
            logger.info('User has insert title name into quick reply 1')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('enter_query')).click()
            logger.info('User has clicked in enter query input box 1')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('enter_query')).send_keys(ExcelReader.read_excel1().get('query_under_quick_reply'))
            logger.info('User has insert a query into quick reply 1')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('add_button1')).click()
            logger.info('User has clicked on add button 1')

            time.sleep(10)
            try:
                element = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('add_reply'))
                driver.execute_script("arguments[0].click();", element)
                logger.info('User has clicked on add reply button to add title in quick reply 2')
            except Exception as e:
                print(e)

            time.sleep(2)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('enter_title_name')).click()
            logger.info('User has clicked in title input box 2')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('enter_title_name')).send_keys(
                ExcelReader.read_excel1().get('title_name_under_quick1'))
            logger.info('User has insert title name into quick reply 2')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('enter_query')).click()
            logger.info('User has clicked in enter query input box 2')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('enter_query')).send_keys(
                ExcelReader.read_excel1().get('query_under_quick_reply'))
            logger.info('User has insert a query into quick reply 2')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('add_button1')).click()
            logger.info('User has clicked on add button 2')

            time.sleep(5)
            #
            element = driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('radio_button1'))
            Utility.explicit_Wait1(element, 'visibility', driver)
            time.sleep(5)
            try:
                driver.execute_script("arguments[0].click();", element)
                logger.info('User has clicked on radio button of one source')
            except Exception as e:
                print(e)

            time.sleep(3)
            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('one_source_input')).click()
            logger.info('User has clicked in source input box')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('one_source_input')).send_keys(ExcelReader.read_excel1().get('answer_by_url1'))
            logger.info('User has entered a source into one source')

            driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('save_button')).click()
            logger.info('User has clicked on save button')

            time.sleep(2)
        except Exception as e:
            logger.info('An exception occurred in verify save a template under flow repository 150')
            allure.attach(self.driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            print(e)
            pytest.fail(e, pytrace=True)