"""
All methods and locators which will use to build tests for ForumPage.
"""

from pages.base_page import BasePage



class ForumPage(BasePage):

    # Locators test_logo_enabled
    _logo = "//*[@id='header']/div[1]/div/a/img"

     # Locators test_page_is_scrollable
    _reviews_footer = "//*[@id='footer-tabbar']/ul[2]/li[4]/a"

    # Locators test_search_engine:
    _search_engine_placeholder = "//*[@id='q']"
    _submit_search_button = "//*[@id='btnSearch']/span"
    _search_value = "Kreta"

    # Text to send
    TEXT_SEND_SEARCH_ENGINE = "Kreta"


    def is_logo_enabled(self):
        return self._driver.find_element_by_xpath(self._logo).is_enabled()

    def is_footer_enabled(self):
        return self._driver.find_element_by_xpath(self._reviews_footer).is_enabled()

    def click_engine_placeholder(self):
        return self._driver.find_element_by_xpath(self._search_engine_placeholder).click()

    def clear_engine_placeholder(self):
        return self._driver.find_element_by_xpath(self._search_engine_placeholder).clear

    def send_text_to_engine_placeholder(self):
        return self._driver.find_element_by_xpath(self._search_engine_placeholder).send_keys(self.TEXT_SEND_SEARCH_ENGINE)

    def click_submit_search_button(self):
        return self._driver.find_element_by_xpath(self._submit_search_button).click()

