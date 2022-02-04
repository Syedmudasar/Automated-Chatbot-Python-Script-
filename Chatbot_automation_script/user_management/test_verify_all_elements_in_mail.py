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

@pytest.mark.usefixtures('setup1')
class Test24:

    def test24_check_sent_mail_content(self):
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

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("")).click()
            logger.info('User has clicked successfully on the mail that is sent to new user')

            text = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('')).text

            if 'HRBOT has invited you to use TELUS International HR-Bot to collaborate with them.' in text:
                logger.info('Mail contains all elements as expected')
            else:
                logger.info('Mail does not contain all elements as expected')

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
            logger.error('An exception occurred in test case verify all elements in mail')
            print(e)
            pytest.fail(e, pytrace=True)