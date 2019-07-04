"""
Test methods for MainPage.
"""

from pages.main_page import MainPage
from tests.main_page_test_template import TestTemplate
from time import sleep

class TestMainPage(TestTemplate):

    def test_logo_available(self):
        """
        Test is checking if logo is displayed at the main site..
        :return: True
        """
        m = MainPage(self.driver)
        assert m.is_logo_enabled() == True

    def test_title(self):
        """
        Test is checking if title of page is correct..
        :return: "Wakacje.pl - Last Minute, Wczasy, Egipt, Turcja, Tunezja, Grecja"
        """
        m = MainPage(self.driver)
        assert m.check_title() == "Wakacje.pl - Last Minute, Wczasy, Egipt, Turcja, Tunezja, Grecja"

    def test_page_is_scrollable(self):
        """
        Test is checking that page is scrollable.
        :return: True
        """
        m = MainPage(self.driver)
        m.scroll_down()
        assert m.is_footer_enabled() == True

    def test_search_regional_office(self):
        """
        Test will be checking search regional detail office
        :return: "gniezno@wakacje.pl"
        """
        k = MainPage(self.driver)
        k.scroll_down()
        k.click_location_dropdown_list()
        k.click_gniezno_dropdown_option()
        sleep(4)
        assert k.find_office_email() == "gniezno@wakacje.pl"


    def test_search_offer(self):
        """
        Test will be checking search offer
        :return: True
        """
        k = MainPage(self.driver)
        k.click_hotel()
        k.click_egypt()
        k.click_hurghada()
        k.click_select()
        k.click_departure()
        k.click_first_august()
        k.click_return()
        k.click_eight_august()
        sleep(3)
        k.click_search()
        sleep(4)
        assert k.is_grand_resort_enabled() == True











