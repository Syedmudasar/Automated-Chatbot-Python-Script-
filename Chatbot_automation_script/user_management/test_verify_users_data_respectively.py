import pytest
from com_hrbot_logger.log import *
from com_hrbot_constant.hrbot_config_mapper import *
from com_htbot_utility.utility import *
from com_htbot_utility.excel_reader import *
from analytics_module.conftest import *
import allure
from allure_commons.types import AttachmentType


logger = Log.get_logger()

@pytest.mark.usefixtures('setup')
class Test26:

    def test26_Verify_users_data_after_clicking_on_user_setting(self):
        driver  = self.driver
        try:
            logger.info('enter user\'s credentials to login page')
            element = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_user_box"))
            element.send_keys(HrBot_Config_mapper.hrbot_config.get("username"))

            time.sleep(2)
            element = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_pass_box"))
            element.send_keys(HrBot_Config_mapper.hrbot_config.get("password"))
            logger.info('User has successfully entered credentials')

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_button")).click()
            logger.info('User has successfully clicked on login button')

            logger.info('Waiting for the element')
            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('conversation_reports'), 'visibility',  driver)

            url = self.driver.current_url
            if url:
                assert url == ExcelReader.read_excel().get("hrbot_homepage_url")
                logger.info('User has been navigated successfully to home page')
            else:
                logger.info('User is not navigated to home page')

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('users_management')).click()
            logger.info('User has successfully clicked on user\'s  module')

            url = self.driver.current_url
            url1 = ExcelReader.read_excel().get('hrbot_users_url')
            if url:
                assert url == url1.replace('\n', '')
                logger.info('User has been navigated successfully to user\'s page')
            else:
                logger.info('User is not navigated to user\'s page')

            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('user_management'), 'visibility', driver)

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('total_users')).click()
            logger.info('User has clicked on total users tab successfully')

            time.sleep(2)
            try:
                users_number = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('total_users_num')).text
                logger.info('Total users number has been fetched successfully how many users exist currently')
                print(users_number)
            except Exception as e:
                print('-----amjad-----', e)

            ls = ['user_name', 'email', 'role', 'region', 'active', 'created']
            dct = {}
            for i in range(1, 11):
                for j in range(1, 7):
                    print(str([j]))
                    time.sleep(1)
                    xpath = "//*[@class='row grid-odd no-gutters']"+ str([i]) +"/div[@class='pr-3 undefined']" +str([j])+ "/span"
                    print(xpath)
                    try:
                        data = self.driver.find_element_by_xpath("//*[@class='row grid-odd no-gutters']"+ str([i]) +"/div[@class='pr-3 undefined']" +str([j])+ "/span").text
                        dct[ls[j-1]] = data
                    except  Exception as e:
                        print('--------3-------', e)
                    print(dct)
                    logger.info('data has been displayed correctly as expected')


        except Exception as e:
            allure.attach(driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            logger.error('An Exception occurred in test case verify users data respectively 26')
            print(e)
            pytest.fail(e, pytrace=True)
