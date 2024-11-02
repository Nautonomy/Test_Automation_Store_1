# IMPORTS
import time

from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class HomePage(BasePage):
    """Page object for Homepage on Automation Test Store."""

    # URLS
    HOME_PAGE_URL = 'https://automationteststore.com/'

    # LOCATORS
    account_link = (By.LINK_TEXT, 'Login or register')
    skincare_button = (By.PARTIAL_LINK_TEXT, 'SKINCARE')
    gift_ideas_button = (By.PARTIAL_LINK_TEXT, 'Gift Ideas & Sets')
    search_bar = (By.ID, 'filter_keyword')
    search_button = (By.CLASS_NAME, 'button-in-search')

    # INITIALIZER
    def __init__(self, driver):
        super().__init__(driver)

    # INTERACTIONS

    def go_to_home_page(self):
        self.go_to_url(self.HOME_PAGE_URL)

    def go_to_login_page(self):
        super().click(self.account_link)

    def go_to_gift_ideas_and_sets(self):
        super().point(self.skincare_button)
        time.sleep(1)
        super().click(self.gift_ideas_button)

    def search_for_night_care_crema(self):
        super().text_and_hit_enter(self.search_bar, 'night care crema')
