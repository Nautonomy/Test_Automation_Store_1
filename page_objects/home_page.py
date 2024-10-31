# IMPORTS
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class HomePage(BasePage):
    """Page object for Homepage on Automation Test Store."""

    # URLS
    HOME_PAGE_URL = 'https://automationteststore.com/'

    # LOCATORS
    account_link = (By.LINK_TEXT, 'Login or register')

    # INITIALIZER
    def __init__(self, driver):
        super().__init__(driver)

    # INTERACTIONS

    def go_to_home_page(self):
        self.go_to_url(self.HOME_PAGE_URL)

    def go_to_login_page(self):
        super().click(self.account_link)

