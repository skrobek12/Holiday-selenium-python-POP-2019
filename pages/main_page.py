"""
All methods and locators which will use to build tests for MainPage.
"""

from pages.base_page import BasePage


class MainPage(BasePage):

    # Locators test_logo_enabled
    _logo = "//*[@id='__next']/div/div/header/figure"

    # Locators test_page_is_scrollable
    _itaka_footer = "//*[@id='__next']/div/div/footer/div[3]/div[2]/a[1]"

    # Locators test_search_regional_office
    _location_dropdown_list = "//*[@id='__next']/div/div/main/div/div[9]/div[2]/span/div/div/div"
    _gniezno_dropdown_option = "//*[@id='__next']/div/div/main/div/div[9]/div[2]/span/div/div/ul/li[40]"
    _office_email = "//*[@id='contactPok']/div[1]/div[2]/div/ul/li[2]/a"

    # Locators test_search_offer
    _hotel = "//*[@id='__next']/div/div/main/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div/div/div/div/div"
    _egypt = "//*[@id='__next']/div/div/main/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div[1]/ul[1]/li[3]"
    _hurghada = "//*[@id='__next']/div/div/main/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/ul/li[2]/label/div"
    _select = "//*[@id='__next']/div/div/main/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/div[3]/a"
    _departure = "//*[@id='__next']/div/div/main/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/input"
    _first_august = "//*[@id='__next']/div/div/main/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div/div/div[2]/div[3]/div[4]"
    _return = "//*[@id='__next']/div/div/main/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div/div[2]/input"
    _eigth_august = "//*[@id='__next']/div/div/main/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div/div[1]/div[2]/div/div/div[1]/div[3]/div[11]"
    _search = "//*[@id='__next']/div/div/main/div/div[1]/div[2]/div[1]/div[2]/div[2]/a"
    _grand_resort = "//*[@id='__next']/div/div/main/div/div[3]/div[2]/section/div[1]/div[1]/article/div/div/div[2]/a/h2"



    def is_logo_enabled(self):
        return self._driver.find_element_by_xpath(self._logo).is_enabled()

    def check_title(self):
        return self._driver.title

    def is_footer_enabled(self):
        return self._driver.find_element_by_xpath(self._itaka_footer).is_enabled()

    def click_location_dropdown_list(self):
        return self._driver.find_element_by_xpath(self._location_dropdown_list).click()

    def click_gniezno_dropdown_option(self):
        return self._driver.find_element_by_xpath(self._gniezno_dropdown_option).click()

    def find_office_email(self):
        return self._driver.find_element_by_xpath(self._office_email).text

    def click_hotel(self):
        return self._driver.find_element_by_xpath(self._hotel).click()

    def click_egypt(self):
        return self._driver.find_element_by_xpath(self._egypt).click()

    def click_hurghada(self):
        return self._driver.find_element_by_xpath(self._hurghada).click()

    def click_select(self):
        return self._driver.find_element_by_xpath(self._select).click()

    def click_departure(self):
        return self._driver.find_element_by_xpath(self._departure).click()

    def click_first_august(self):
        return self._driver.find_element_by_xpath(self._first_august).click()

    def click_return(self):
        return self._driver.find_element_by_xpath(self._return).click()

    def click_eight_august(self):
        return self._driver.find_element_by_xpath(self._eigth_august).click()

    def click_search(self):
        return self._driver.find_element_by_xpath(self._search).click()

    def is_grand_resort_enabled(self):
        return self._driver.find_element_by_xpath(self._grand_resort).is_enabled()









