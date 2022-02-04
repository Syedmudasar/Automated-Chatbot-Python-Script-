import pytest
from com_hrbot_logger.log import Log
from com_hrbot_constant.hrbot_config_mapper import HrBot_Config_mapper
from analytics_module.conftest import *
from com_htbot_utility.excel_reader import *
from allure_commons.types import AttachmentType
import time
import allure


logger = Log.get_logger()

@pytest.mark.usefixtures('setup')
class Test31:

    flag = False

    def test31_Verify_pagination(self):
        try:
            driver = self.driver

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
            if url:
                assert url == ExcelReader.read_excel().get("hrbot_homepage_url")
                logger.info('User has been navigated successfully to home page')
            else:
                logger.info('User is not navigated to home page')

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('users_management')).click()
            logger.info('User has successfully clicked on user\'s module')

            url = self.driver.current_url
            url1 = ExcelReader.read_excel().get('hrbot_users_url')
            if url:
                assert url == url1.replace('\n', '')
                logger.info('User has been navigated successfully to user\'s page')
            else:
                logger.info('User is not navigated to user\'s page')

            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('user_management'), 'visibility', driver)


            active_users = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('activate_users_num')).text
            logger.info('Active users is fetched successfully')
            print(active_users)

            if int(active_users) < 10:
                flag = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('next_page1')).is_enabled()
                logger.info('')

                if flag == True:
                    logger.info('next button is disable as expected')
                else:
                    logger.info('next button is not disable')
            else:
                self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('next_page1')).click()
                logger.info('User has clicked on next button successfully')

                time.sleep(3)
                self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('back_page1')).click()
                logger.info('User has clicked on back button successfully')

                time.sleep(3)
                self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('last_page1')).click()
                logger.info('User has clicked on last button to move to last page')

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), AttachmentType.PNG)
            logger.error('An Error occurred in verify pagination 31')
            print(e)
            pytest.fail(e, pytrace=True)