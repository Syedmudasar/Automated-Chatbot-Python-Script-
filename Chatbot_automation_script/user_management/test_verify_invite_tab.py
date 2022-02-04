from com_hrbot_modules.launchEnvironment import *
from analytics_module.conftest import *
from com_htbot_utility.excel_reader import *
from com_htbot_utility.utility import *
from allure_commons.types import AttachmentType
from com_hrbot_logger.log import Log
import allure
import time


logger = Log.get_logger()

@pytest.mark.usefixtures('setup')
class Test11:

    def test11_validate_invite_tab_shows_correctly(self):
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
            Utility.explicit_Wait(HrBot_Config_mapper.hrbot_locators.get('conversation_reports'), 'visibility', self.driver)

            url = self.driver.current_url
            if url:
                assert url == ExcelReader.read_excel().get("hrbot_homepage_url")
                logger.info('User has been navigated successfully to home page')
            else:
                logger.info('User is not navigated to home page')

            Utility.click_on_element(HrBot_Config_mapper.hrbot_locators.get('users_setting'))
            # self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('users_setting')).click()
            # logger.info('User has successfully clicked on user\'s setting module')

            url = self.driver.current_url
            if url:
                assert url == ExcelReader.read_excel().get('hrbot_users_url')
                logger.info('User has been successfully to user\'s page')
            else:
                logger.info('User is not navigated to user\'s page')

            value = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('invited_users_num')).text
            logger.info('User has extracted how many users invited users')
            print(value)

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('invited_tab')).click()
            logger.info('User has successfully clicked on invited tab from tab list')

            logger.info('The page is being loaded wait unit page to be loaded')
            Utility.explicit_Wait(HrBot_Config_mapper.hrbot_locators.get('user_management'), 'visibility', self.driver)



            list_activate_user = []
            counter = 10
            counter1 = 10
            end_index = int(value)
            start_index = 1
            logger.info('started count active users')
            for i in range(start_index, end_index + 1):
                try:
                    if i < 11:
                        logger.info('---------start--------')
                        xpath = "//*[@class='row grid-odd no-gutters']" + str([i]) + "/div[@class='pr-3']/span"
                        list_activate_user.append(self.driver.find_element_by_xpath(xpath).text)
                    elif i >= 11:
                        #  print("//*[@class='row grid-odd no-gutters']" + str([i-counter1]) + "/div[@class='pr-3']/span")
                        xpath1 = "//*[@class='row grid-odd no-gutters']" + str([i - counter1]) + "/div[@class='pr-3']/span"
                        list_activate_user.append(self.driver.find_element_by_xpath(xpath1).text)
                        if str(0) in str(i):
                            counter1 += 10
                    elif len(list_activate_user) == int(value):
                        break
                except InterruptedError as e:
                    print(e)
                    logger.error('----------error----------')
                if counter == len(list_activate_user):
                    self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("next_page1")).click()
                    time.sleep(5)
                    logger.info('User has clicked on custom pagination to move to next page')
                    counter += 10

            if length and value:
                assert value == length
                logger.info('both are equal as expected')
            else:
                logger.info('Invite number and manual counting both are not equal so there is an exception there')
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            logger.error('An Error occurred in verify the invite tab is showing active user as many as shown above active')
            print(e)
            pytest.fail(e, pytrace=True)