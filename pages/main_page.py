"""
All methods and locators which will use to build tests for MainPage.
"""

from pages.base_page import BasePage


class MainPage(BasePage):

    # Locators test_logo_enabled
    _logo = "/html//div[@class='mainContainer']//a[@href='/']/img[@alt='wakacje.pl']"

    # Locators test_page_is_scrollable
    _itaka_footer = "/html//div[@class='mainContainer']/div[@class='footer']//a[@href='/biuro/itaka/']"

    # Locators test_search_regional_office
    _location_dropdown_list = "/html//span[@id='pokCitySelectBoxIt']"
    _gniezno_dropdown_option = "//*[@id='39']/a"
    _office_email = "/html//div[@id='contactPok']//ul[@class='contactList']//a[@href='mailto:gniezno@wakacje.pl']"

    # Locators test_search_offer
    _hotel = "//*[@id='countrySelectBoxItText']"
    _egypt = "//*[@id='popularAll']/li[3]/label"
    _hurghada = "//*[@id='countryCont-37']/li[3]/label"
    _select = "//*[@id='directionsLbClose']"
    _departure = "//*[@id='departureDate']"
    _first_november = "//*[@id='ui-datepicker-div']/div[2]/table/tbody/tr[1]/td[5]/a"
    _return = "//*[@id='arrivalDate']"
    _eigth_november = "//*[@id='ui-datepicker-div']/div[1]/table/tbody/tr[2]/td[5]/a"
    _search = "//*[@id='submitSearchBox']"
    _minamark_resort = "//*[@id='promoOfferOuterCont']/div/div[1]/div/a/span[1]"


    def is_logo_enabled(self):
        return self._driver.find_element_by_xpath(self._logo).is_enabled()

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

    def click_first_november(self):
        return self._driver.find_element_by_xpath(self._first_november).click()

    def click_return(self):
        return self._driver.find_element_by_xpath(self._return).click()

    def click_eight_november(self):
        return self._driver.find_element_by_xpath(self._eigth_november).click()

    def click_search(self):
        return self._driver.find_element_by_xpath(self._search).click()

    def is_minamark_resort_enabled(self):
        return self._driver.find_element_by_xpath(self._minamark_resort).is_enabled()









