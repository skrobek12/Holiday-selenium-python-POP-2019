"""
All methods and locators which will use to build tests for ForumPage.
"""

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ForumPage(BasePage):

    # Locators test_logo_enabled
    _logo = "//*[@id='__next']/div/div/header/figure"

     # Locators test_page_is_scrollable
    _reviews_footer = "//*[@id='footer-tabbar']/ul[2]/li[4]/a"

    # Locators test_search_engine:
    _search_engine_placeholder = "//*[@id='q']"
    _submit_search_button = "//*[@id='btnSearch']/span"
    _search_value = "Kreta"

    # Locators test_sign_in_on_account
    _sign_in = "//*[@id='lnkLoginSignupMenu']"
    _username = "//*[@id='idLoginUserName']"
    _password = "//*[@id='idLoginPassword']"
    _submit = "//*[@id='idLoginBtn']"
    _user = "//*[@id='lnkUsernameMenu']/span[1]"
    _log_out = "//*[@id='main-navbar']/ul[2]/li[4]/ul/li[4]/a/span"

    # Text to send
    TEXT_SEND_SEARCH_ENGINE = "Kreta"
    TEXT_SEND_USERNAME = "skrobek12"
    TEXT_SEND_PASSWORD = "skrobencjusz"



    def is_logo_enabled(self):
        return self._driver.find_element_by_xpath(self._logo).is_enabled()

    def check_title(self):
        return self._driver.title

    def is_footer_enabled(self):
        return self._driver.find_element_by_xpath(self._reviews_footer).is_enabled()

    def click_engine_placeholder(self):
        return self._driver.find_element_by_xpath(self._search_engine_placeholder).click()

    def clear_engine_placeholder(self):
        return self._driver.find_element_by_xpath(self._search_engine_placeholder).clear

    def send_text_to_engine_placeholder(self):
        return self._driver.find_element_by_xpath(self._search_engine_placeholder).send_keys(self.TEXT_SEND_SEARCH_ENGINE)

    def click_submit_search_button(self):
        wait = WebDriverWait(self._driver, 5)
        return wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self._submit_search_button))).click()

    def click_sign_in(self):
        return self._driver.find_element_by_xpath(self._sign_in).click()

    def click_username(self):
        return self._driver.find_element_by_xpath(self._username).click()

    def clear_username(self):
        return self._driver.find_element_by_xpath(self._username).clear

    def send_text_to_username(self):
        return self._driver.find_element_by_xpath(self._username).send_keys(self.TEXT_SEND_USERNAME)

    def click_password(self):
        return self._driver.find_element_by_xpath(self._password).click()

    def clear_password(self):
        return self._driver.find_element_by_xpath(self._password).clear

    def send_text_to_password(self):
        return self._driver.find_element_by_xpath(self._password).send_keys(self.TEXT_SEND_PASSWORD)

    def click_submit(self):
        return self._driver.find_element_by_xpath(self._submit).click()

    def click_user(self):
        return self._driver.find_element_by_xpath(self._user).click()

    def is_account_enabled(self):
        return self._driver.find_element_by_xpath(self._log_out).is_enabled()