import pytest
from com_hrbot_logger.log import *
from com_hrbot_constant.hrbot_config_mapper import *
from com_htbot_utility.utility import *
from com_htbot_utility.excel_reader import *
from analytics_module.conftest import *
from allure_commons.types import AttachmentType
import allure
import time

logger = Log.get_logger()

@pytest.mark.usefixtures('setup')
class Test23:

    def test23_Verify_mail_sent_successfully(self):
        try:
            logger.info('enter user\'s credentials to login page')
            element = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_user_box"))
            element.send_keys(HrBot_Config_mapper.hrbot_config.get("username"))

            time.sleep(2)
            element = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_pass_box"))
            element.send_keys(HrBot_Config_mapper.hrbot_config.get("password"))
            logger.info('User has successfully entered credentials')

            Utility.click_on_element(HrBot_Config_mapper.hrbot_locators.get('login_button'), self.driver)
            #self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_button")).click()
            logger.info('User has successfully clicked on login button')

            logger.info('Waiting for the element')
            Utility.explicit_Wait(HrBot_Config_mapper.hrbot_locators.get('conversation_reports'), self.driver)

            url = self.driver.current_url
            if url:
                assert url == ExcelReader.read_excel().get("hrbot_homepage_url1")
                logger.info('User has been navigated successfully to home page')
            else:
                logger.info('User is not navigated to home page')

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('users_management')).click()
            logger.info('User has successfully clicked on user\'s setting module')

            url = self.driver.current_url

            if url:
                assert url == ExcelReader.read_excel().get('hrbot_users_url1')
                logger.info('User has been navigated successfully to user\'s page')
            else:
                logger.info('User is not navigated to user\'s page')

            Utility.explicit_Wait(HrBot_Config_mapper.hrbot_locators.get('user_management'), self.driver)

            before_invited_number = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('invited_users_num')).text
            logger.info('User has extracted how many users invited users 1')
            print(before_invited_number)

            for i in range(2):
                time.sleep(2)
                if int(before_invited_number) < 1:

                    self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('invite_users_button')).click()
                    logger.info('user has clicked successfully on invite user button')

                    element = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('user_invitation_mail_box'))
                    element.send_keys(HrBot_Config_mapper.hrbot_config.get('google_mail'))
                    logger.info('User has entered mail id to invite a new users')

                    self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('radio_button')).click()
                    logger.info('User has clicked on radio button in order to decide role of new user')

                    time.sleep(2)
                    self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('region_drop_down')).click()
                    logger.info('User has clicked on drop down for region')

                    time.sleep(2)
                    self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('region_type')).click()
                    logger.info('User has selected successfully the region')

                    time.sleep(2)
                    self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('send_invitation')).click()
                    logger.info('User has been sent invitation')

                    break
                else:
                    self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('invited_tab')).click()
                    logger.info('User has clicked successfully on invite tab')

                    time.sleep(2)
                    self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('invalidate_dots')).click()
                    logger.info('User has successfully clicked on invalidate dots ')

                    self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('invalidate_button')).click()
                    logger.info('User has successfully clicked on invalidate button')

                    time.sleep(2)
                    before_invited_number1 = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('invited_users_num')).text
                    logger.info('User has extracted how many users invited users 1')
                    before_invited_number = before_invited_number1
                    print(before_invited_number)

            time.sleep(2)
            after_invited_number = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('invited_users_num')).text
            logger.info('User has extracted how many users invited users 2')
            print(after_invited_number)

            if after_invited_number:
                assert before_invited_number < after_invited_number
                logger.info('new user is invited successfully')
            else:
                logger.info('there is an error while invite user')

        except Exception as e:
            allure('screenshots', self.driver.get_screenshot_as_png(), AttachmentType.PNG)
            logger.error('An Error occurred in Verify_mail_sent_successfully 22')
            print(e)

@pytest.mark.usefixtures('setup1')
class Test24:

    def test24_check_sent_mail(self):
        try:
            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('mail_input_box')).send_keys(HrBot_Config_mapper.hrbot_config.get('google_mail_id'))
            # element.send_keys(HrBot_Config_mapper.hrbot_config.get('google_mail_id'))
            logger.info('Email id is entered to input box')

            element = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('password_input_box'))
            element.send_keys(HrBot_Config_mapper.hrbot_config.get('google_mail_password'))
            logger.info('Password is entered to password input box')

            element = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('sign_in'))
            element.click()
            logger.info('User has signed in')

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("continue")).click()

            time.sleep(5)
            ls = []
            path = "//*[@class='zA zE']" + str([1]) + "/td[5]/div[2]/span/span[@class='zF']"
            ls.append(self.driver.find_element_by_xpath(path).text)
            print(ls)
            if 'bot-noreply' in ls:
                 logger.info('Invitation Mail is sent successfully to new user ')
            else:
                logger.info('Invitation mail not found there')

            # mail_title = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("unread_mail")).text

            # logger.info('Email text has been fetched from mail inbox')
            #
            # if mail_title:
            #     assert mail_title == 'bot-noreply'
            #     logger.info('Mail is sent to the user successfully')
            # else:
            #     logger.info('Mail is not sent to the user')
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            logger.error('An exception occurred in test case check mail is sent ot not')
            print(e)
            pytest.fail(e, pytrace=True)