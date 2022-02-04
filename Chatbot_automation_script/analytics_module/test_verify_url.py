from com_htbot_utility.excel_reader import ExcelReader
from com_hrbot_logger.log import Log
import pytest
from analytics_module.conftest import *
from allure_commons.types import AttachmentType
import allure
import time

logger = Log.get_logger()


@pytest.mark.usefixtures("setup")
class Test1:

    def test_verify_url(self):
        try:

            url = self.driver.current_url
            print(url)
            assert url == ExcelReader.read_excel().get('login_page_url')
            logger.info('User has been navigated successfully on login page')

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), 'screenshots', AttachmentType.PNG)
            logger.error('An Error occurred in verify url Test case ')
            print(e)
            pytest.fail(e, pytrace=True)


