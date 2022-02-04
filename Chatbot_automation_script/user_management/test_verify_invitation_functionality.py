import pytest
from com_hrbot_logger.log import *
from com_hrbot_constant.hrbot_config_mapper import *
from com_htbot_utility.utility import *
from com_htbot_utility.excel_reader import *
from allure_commons.types import *
from analytics_module.conftest import *
import allure


logger = Log.get_logger()

@pytest.mark.usefixtures('setup')
class Test21:

    def test21_Verify_Send_invitation_button(self):
        driver =  self.driver
        try:
            logger.info('enter user\'s credentials to login page')
            element = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_user_box"))
            element.send_keys(HrBot_Config_mapper.hrbot_config.get("username"))

            element = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_pass_box"))
            element.send_keys(HrBot_Config_mapper.hrbot_config.get("password"))
            logger.info('User has successfully entered credentials')

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_button")).click()
            logger.info('User has successfully clicked on login button')

            logger.info('Waiting for the element')
            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('conversation_reports'), 'visibility', driver)

            url = self.driver.current_url
            url1 = ExcelReader.read_excel().get("hrbot_homepage_url")
            if url:
                assert url == url1.replace('\n', '')
                logger.info('User has been navigated successfully to home page')
            else:
                logger.info('User is not navigated to home page')

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('users_management')).click()
            logger.info('User has successfully clicked on user\'s setting module')

            url = self.driver.current_url
            url1 = ExcelReader.read_excel().get('hrbot_users_url')
            if url:
                assert url == url1.replace('\n', '')
                logger.info('User has been navigated successfully to user\'s page')
            else:
                logger.info('User is not navigated to user\'s page')

            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('user_management'), 'visibility', driver)

            before_invited_number = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('invited_users_num')).text
            logger.info('User has extracted how many users invited users')
            print(before_invited_number)

            i = 0
            while i < 2:
                if int(before_invited_number) > 0:
                    self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('invited_tab')).click()
                    logger.info('user has clicked successfully on invite tab button')

                    time.sleep(2)
                    self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('quick_action')).click()
                    logger.info('User has clicked on successfully quick_action')

                    time.sleep(2)
                    self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('invalidate_button')).click()
                    logger.info('User has clicked on invalidate button')

                    time.sleep(2)
                    before_invited_number = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('invited_users_num')).text
                    logger.info('User has extracted how many users invited users')
                    print(before_invited_number)
                else:
                    self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('invite_users_button')).click()
                    logger.info('user has clicked successfully on invite user button')

                    element = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('user_invitation_mail_box'))
                    element.send_keys(HrBot_Config_mapper.hrbot_config.get('mail_id'))
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
                i += 1

            # if after_invited_number:
            #     assert int(before_invited_number) < int(after_invited_number)
            #     logger.info('new user is invited successfully')
            # else:
            #     logger.info('there is an error while invite user')

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            logger.error('An Error occurred in Verify Send invitation button 21')
            print(e)
            pytest.fail(e, pytrace=True)

