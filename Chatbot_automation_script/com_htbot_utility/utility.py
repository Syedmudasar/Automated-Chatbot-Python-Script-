from com_hrbot_constant.constant import *
from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from com_hrbot_logger.log import Log
from com_htbot_utility.excel_reader import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import unittest
import time
import random
import string


parser = ConfigParser()
logger = Log.get_logger()


# noinspection PyBroadException
class Utility:

    @staticmethod
    def get_data(string):
        try:
            data = parser.read(string)
        except FileNotFoundError as file:
            print(file)
        sect = parser.sections()
        return sect

    @staticmethod
    def config_selection_map(section):
        dict1 = {}
        values = parser.items(section)
        for tuple in values:
            dict1[tuple[0]] = tuple[1]
        return dict1


    @staticmethod
    def explicit_Wait1(element, for_what, driver):
        try:
            if for_what == 'visibility':
                logger.info('The page is being loaded for the elements')
                time.sleep(3)
                try:
                    wait = WebDriverWait(driver, 10)
                except Exception as e:
                    print('------amjad-------', e)
                try:
                    wait.until(ec.visibility_of_element_located((By.XPATH, element)))
                    logger.info('The page is loaded successfully')
                except Exception as e:
                    print('--------amjad2------', e)
            elif for_what == 'clickable':
                logger.info('The element is getting click able')
                wait = WebDriverWait(driver, 10)
                wait.until(ec.element_to_be_clickable(By.XPATH, element))
                logger.info('The Button is visible there')
            else:
                logger.info('')
        except Exception as e:
            print(e)

    staticmethod
    def click_on_element(elem, driver):
        try:
            userName = driver.find_element_by_xpath(By.XPATH, elem)
            driver.execute_script("arguments[0].click();", userName)
        except Exception as e:
            logger.error('')

    @staticmethod
    def random_number(end_n):
        num = random.randint(1, int(end_n))
        return num

    @staticmethod
    def random_number1(number):
        num = random.randint(1, number)
        return num

    @staticmethod
    def randomString(stringLength):
        letters = string.ascii_letters.lower()
        return ''.join(random.choice(letters) for i in range(stringLength))

    @staticmethod
    def create_sub_folder(list_folder_names, driver):
        counter = 0
        path1 = ''
        for names in list_folder_names:
            counter += 1
            print(names)
            folder = ExcelReader.read_excel2().get('folder_name')
            logger.info('All folder names has been fetched successfully')
            if folder == names:
                try:
                    path1 = HrBot_Config_mapper.hrbot_locators.get('folder_name')
                    path1.format(folder)
                except Exception as e:
                    print('------amjad-------', e)
                try:
                    time.sleep(2)
                    action = ActionChains(driver)
                    element = driver.find_element_by_xpath(path1)
                    action.drag_and_drop_by_offset(element, 200, 0).perform()
                    logger.info('User has dragged and dropped cursor on element')
                    time.sleep(4)
                    #  x = "((//*[@class='rst__rowToolbar'])[{}]//div[@class='rst__rowNodeAdd'])/span[@class='text-btnTitle']".format(counter)
                    path = HrBot_Config_mapper.hrbot_locators.get('new_folder')
                    exact_path = path.format(counter)
                    driver.find_element_by_xpath(exact_path).click()
                    logger.info('User has clicked on new sub folder')
                    time.sleep(3)
                    driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('enter_folder_name')).send_keys(
                        ExcelReader.read_excel2().get('sub_folder_name'))
                    logger.info('User has entered sub folder name as : ')
                    time.sleep(5)
                    driver.find_element_by_xpath(HrBot_Config_mapper.hrbot_locators.get('create_folder')).click()
                    break
                except Exception as e:
                    print('An Exception occurred in create sub folder method :', e)

    @staticmethod
    def move_to_target_element(xpath, web_driver):
        action = ActionChains(web_driver)
        try:
            action.move_to_element(xpath).perform()
            # web_driver.find_element_by_xpath(xpath).send_keys(Keys.DOWN)
            time.sleep(4)
            # web_driver.click()
            # action = ActionChains(web_driver)
            # action.move_to_element(xpath).perform()
            # web_driver.find_element_by_xpath(xpath).click()
        except Exception as e:
            print('-------<amjad>------1', e)

    @staticmethod
    def verify_urls(self, region_name, driver):
        if region_name == 'Small Talk':
            url = ExcelReader.read_excel().get('hrbot_small_talk_url')
            url1 = driver.current_url
            self.assertEqual(url, url1)
            logger.info('User has been navigated to a particular region page')
        elif region_name == 'TICA-El Salvador':
            url = ExcelReader.read_excel().get('hrbot_tica_ei_salvador_url')
            url1 = driver.current_url
            self.assertEqual(url, url1)
            logger.info('User has been navigated to a particular region page')
        elif region_name == 'TICA-Guatemala':
            url = ExcelReader.read_excel().get('hrbot_tica_guatemala_url')
            url1 = driver.current_url
            self.assertEqual(url, url1)
            logger.info('User has been navigated to a particular region page')
        elif region_name == 'TIC-Canada':
            url = ExcelReader.read_excel().get('hrbot_tic_canada_url')
            url1 = driver.current_url
            self.assertEqual(url, url1)
            logger.info('User has been navigated to a particular region page')
        elif region_name == 'TIE-Bulgaria':
            url = ExcelReader.read_excel().get('hrbot_tie_bulgaria_url')
            url1 = driver.current_url
            self.assertEqual(url, url1)
            logger.info('User has been navigated to a particular region page')
        elif region_name == 'TIE-Ireland':
            url = ExcelReader.read_excel().get('hrbot_tie_ireland_url')
            url1 = driver.current_url
            self.assertEqual(url, url1)
            logger.info('User has been navigated to a particular region page')
        elif region_name == 'TIE-Romania':
            url = ExcelReader.read_excel().get('hrbot_tie_romania_url')
            url1 = driver.current_url
            self.assertEqual(url, url1)
            logger.info('User has been navigated to a particular region page')
        elif region_name == 'TIE-United Kingdom':
            url = ExcelReader.read_excel().get('hrbot_tie_united_kingdom_url')
            url1 = driver.current_url
            self.assertEqual(url, url1)
            logger.info('User has been navigated to a particular region page')
        elif region_name == 'TII-India':
            url = ExcelReader.read_excel().get('hrbot_tii_india_url')
            url1 = driver.current_url
            self.assertEqual(url, url1)
            logger.info('User has been navigated to a particular region page')
        elif region_name == 'TI-Philippines':
            url = ExcelReader.read_excel().get('hrbot_ti_philippines_url')
            url1 = driver.current_url
            self.assertEqual(url, url1)
            logger.info('User has been navigated to a particular region page')
        elif region_name == 'TIUS-USA':
            url = ExcelReader.read_excel().get('hrbot_tius_usa_url')
            url1 = driver.current_url
            self.assertEqual(url, url1)
            logger.info('User has been navigated to a particular region page')
        else:
            logger.info('Not any region found ::: {}'.format(region_name))

    @staticmethod
    def choose_random_region(num, path, web_driver):
            xpath = path.format(num)
            region_name1 = web_driver.find_element_by_xpath(xpath).text
            web_driver.find_element_by_xpath(xpath).click()
            logger.info('user has selected region as ::: {}'.format(region_name1))

    @staticmethod
    def choose_random_region1(num, path, web_driver):
        xpath = path.format(num)
        region_name1 = web_driver.find_element_by_xpath(xpath).text
        web_driver.find_element_by_xpath(xpath).click()
        logger.info('user has selected region as ::: {}'.format(region_name1))
        return region_name1



    @staticmethod
    def choose_random_region2(num, path, web_driver):
        xpath = path.format(num)
        region_name1 = web_driver.find_element_by_xpath(xpath).text
        # web_driver.find_element_by_xpath(xpath).click()
        logger.info('user has selected region as ::: {}'.format(region_name1))
        return region_name1


    @staticmethod
    def change_tab(web_driver):
        try:
            action = ActionChains(web_driver)
            action.key_down(Keys.CONTROL).key_down(Keys.TAB).key_up(Keys.TAB).key_up(Keys.CONTROL).perform()
            logger.info('User has changed the tab')
        except Exception as e:
            print(e)

    @staticmethod
    def switch_windows(windows, web_driver):
        size = len(windows)
        for i in range(size):
            if windows[i] != web_driver.current_window_handle:
                web_driver.switch_to.window(windows[i])



