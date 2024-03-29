"""
Test methods for ForumPage.
"""

from pages.forum_page import ForumPage
from tests.forum_page_test_template import TestTemplate


class TestForumPage(TestTemplate):

    def test_logo_available(self):
        """
        Test is checking if logo is displayed at the main site..
        :return: True
        """
        m = ForumPage(self.driver)
        assert m.is_logo_enabled() == True

    def test_title(self):
        """
        Test is checking if title of page is correct..
        :return: "Forum - Forum Wakacje.pl"
        """
        m = ForumPage(self.driver)
        assert m.check_title() == "Forum - Forum Wakacje.pl"

    def test_page_is_scrollable(self):
        """
        Test is checking that page is scrollable.
        :return: True
        """
        m = ForumPage(self.driver)
        m.scroll_down()
        assert m.is_footer_enabled() == True

    def test_search_engine(self):
        """
        After clicking on the button open search, we will be input "Kreta" word into search engine to checking that
        search engine is working correctly. Finally we should be on the search results card.
        :return: "Search Results - Forum Wakacje.pl"
        """
        m = ForumPage(self.driver)
        m.click_engine_placeholder()
        m.clear_engine_placeholder()
        m.send_text_to_engine_placeholder()
        m.click_submit_search_button()
        assert m.check_title() == "Search Result - Forum Wakacje.pl"







