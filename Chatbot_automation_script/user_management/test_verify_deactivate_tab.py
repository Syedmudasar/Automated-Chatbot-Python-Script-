from analytics_module.conftest import *
from com_htbot_utility.excel_reader import *
from com_htbot_utility.utility import *
from com_hrbot_constant.hrbot_config_mapper import *
from com_hrbot_logger.log import Log
from allure_commons.types import AttachmentType
import allure
import time

logger = Log.get_logger()

@pytest.mark.usefixtures('setup')
class Test10:


    def test10_validate_deactivate_tab_shows_users_correctly(self):
        driver = self.driver
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
            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('conversation_reports'), 'visibility',  driver)

            url = self.driver.current_url
            url1 = ExcelReader.read_excel().get("hrbot_homepage_url")
            if url:
                assert url == url1.replace('\n', '')
                logger.info('User has been navigated successfully to home page')
            else:
                logger.info('User is not navigated to home page')

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('users_setting')).click()
            logger.info('User has successfully clicked on user\'s module')

            url = self.driver.current_url
            url1 = ExcelReader.read_excel().get('hrbot_users_url')
            if url:
                assert url == url1.replace('\n', '')
                logger.info('User has been successfully to user\'s page')
            else:
                logger.info('User is not navigated to user\'s page')

            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('user_management'), 'visibility', driver)

            deactivate_users = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('deactivate_users_num')).text
            logger.info('User has extracted how many users deactivated')
            print(deactivate_users)

            # Utility.click_on_element(HrBot_Config_mapper.hrbot_locators.get('deactivate_tab'), self.driver)

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('deactivate_tab')).click()
            logger.info('User has successfully clicked on deactivated tab from tab list')

            logger.info('The page is being loaded wait unit page to be loaded')
            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('user_management'), 'visibility', driver)

            list_activate_user = []
            counter = 10
            counter1 = 10
            end_index = int(deactivate_users)
            start_index = 1
            logger.info('started count active users')
            for i in range(start_index, end_index + 1):
                try:
                    if i < 11:
                        logger.info('---------start--------')
                        xpath = "//*[@class='row grid-odd no-gutters']" + str([i]) + "/div[@class='pr-3 undefined']/span"
                        list_activate_user.append(self.driver.find_element_by_xpath(xpath).text)
                    # elif i >= 11:
                    #     #  print("//*[@class='row grid-odd no-gutters']" + str([i-counter1]) + "/div[@class='pr-3']/span")
                    #     xpath1 = "//*[@class='row grid-odd no-gutters']" + str([i - counter1]) + "/div[@class='pr-3']/span"
                    #     list_activate_user.append(self.driver.find_element_by_xpath(xpath1).text)
                    #     if str(0) in str(i):
                    #         counter1 += 10
                    elif len(list_activate_user) == int(deactivate_users):
                        break
                except InterruptedError as e:
                    print(e)
                    logger.error('----------error----------')
                if counter == len(list_activate_user):
                    self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("next_page1")).click()
                    time.sleep(5)
                    logger.info('User has clicked on custom pagination to move to next page')
                    counter += 10

            length = len(list_activate_user)
            if length and deactivate_users:
                assert int(deactivate_users) == length
                logger.info('both are equal as expected')
            else:
                logger.info('Deactivate number and manual counting both are not equal so there is an exception there')
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            logger.error('An Error occurred in verify the deactivate tab is showing active user as many as shown above active')
            print(e)
            pytest.fail(e, pytrace=True)