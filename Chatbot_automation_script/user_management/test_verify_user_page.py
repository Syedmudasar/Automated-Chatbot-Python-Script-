from com_hrbot_modules.launchEnvironment import *
from analytics_module.conftest import *
from com_hrbot_logger.log import *
from com_htbot_utility.excel_reader import *
from allure_commons.types import AttachmentType
import allure
import pytest

logger = Log.get_logger()

@pytest.mark.usefixtures('setup')
class Test8:

    url = None
    url1 = None
    # validate user's page after clicking on user's setting
    # noinspection PyBroadException
    def test8_validate_users_page(self):

        try:
            logger.info('enter user\'s credentials to login page')
            element = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_user_box"))
            element.send_keys(HrBot_Config_mapper.hrbot_config.get("username"))

            element = self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_pass_box"))
            element.send_keys(HrBot_Config_mapper.hrbot_config.get("password"))
            logger.info('User has successfully entered credentials ')

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("login_button")).click()
            logger.info('user has successfully clicked on login button')
            driver = self.driver
            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('conversation_reports'), 'visibility', driver)

            url = self.driver.current_url
            print(url)

            if url:
                assert url == ExcelReader.read_excel().get("hrbot_homepage_url")
                logger.info('User has been navigated successfully to home page ')
            else:
                logger.info('User is not navigated to home page')

            self.driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get("users_setting")).click()
            logger.info('User has successfully clicked on user\'s setting module')

            Utility.explicit_Wait1(HrBot_Config_mapper.hrbot_locators.get('user_management'), "visibility", self.driver)

            url = self.driver.current_url
            print(url)
            if url:
                url1 = ExcelReader.read_excel().get("hrbot_users_url")
                print('----------', url, url1)
                if url != url1:
                    assert url == url1.replace('\n', '')
                    logger.info('User has been navigated successfully to user\'s page')
                else:
                    logger.info('url equals')
            else:
                logger.info('User is not navigated to user\'s page')

        except Exception as e:
            #Attachment('screenshot', self.driver.save_screenshot(), type=AttachmentType.PNG)
            # pytest -v -s --html=/home/mamjad/PycharmProjects/hrbot_automation_script/com_hrbot_reports/test.html
            # --self-contained-html test_automation_suite.py
            allure.attach(self.driver.save_screenshot(), 'screenshots', AttachmentType.PNG)
            logger.error('An Error occurred in verify user\'s page')
            print(e)
            pytest.fail(e, pytrace=True)

