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
class Test27:

    def test27_Verify_assc_desc_order_by_sort_functionality(self):
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
            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('conversation_reports'), 'visibility', self.driver)

            url = self.driver.current_url
            url1 = ExcelReader.read_excel().get('hrbot_homepage_url')
            if url:
                assert url == url1.replace('\n', '')
                logger.info('User has been navigated successfully to home page')
            else:
                logger.info('User is not navigated to home page')

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('users_management')).click()
            logger.info('User has successfully clicked on user\'s module')

            time.sleep(2)
            url = self.driver.current_url
            url1 = ExcelReader.read_excel().get('hrbot_users_url')
            if url:
                assert url == url1.replace('\n', '')
                logger.info('User has been navigated successfully to user\'s page')
            else:
                logger.info('User is not navigated to user\'s page')

            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('user_management'), 'visibility', self.driver)

            # collect users name after descending order

            time.sleep(2)
            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('sort_by')).click()
            logger.info('User has clicked on sort by button successfully')

            time.sleep(2)
            try:
                self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('sort_by_role')).click()
                logger.info('User has selected a particular option in order to sort users data accordingly')
            except Exception as e:
                print('-------amjad-------', e)

            time.sleep(1)
            try:
                self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('descending_order')).click()
                logger.info('User has sorted date descending order')
            except Exception as e:
                print('--------amjad2-----', e)

            ls = []
            for i in range(1, 11):
                try:
                    path = "//*[@class='row grid-odd no-gutters']" + str([i]) + "/div/span"
                    print(path)
                    ls.append(self.driver.find_element_by_xpath(path).text)
                except Exception as e:
                    print('---------amjad3------', e)

            print('before sorting', ls)
            ls.sort()
            print('after sorting', ls)

            # collect data after ascending order by name

            # time.sleep(2)
            # try:
            #     self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('sort_by')).click()
            #     logger.info('User has clicked on sort by button successfully')
            # except Exception as e:
            #     print('-----amjad4-----', e)
            # time.sleep(2)
            # try:
            #     self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('sort_by_role')).click()
            #     logger.info('User has selected a particular option in order to sort users data accordingly')
            # except Exception as e:
            #     print('-------amjad-------', e)
            time.sleep(2)
            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('ascending_order')).click()
            logger.info('User has sorted users data ascending order')

            # self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('')).click()
            #
            # self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('')).click()

            time.sleep(2)
            ls1 = []
            for i in range(1, 11):
                path = "//*[@class='row grid-odd no-gutters']" + str([i]) + "/div/span"
                ls1.append(self.driver.find_element_by_xpath(path).text)

            print('sorting order', ls1)

            if ls == ls1:
                logger.info('both functionality are working fine as expected')
            else:
                logger.info('not working ')
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            logger.error('An Exception occurred in test case verify ascending and descending order 27')
            print(e)
            pytest.fail(e, pytrace=True)
