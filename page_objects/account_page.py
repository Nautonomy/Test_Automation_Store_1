# IMPORTS

from page_objects.base_page import BasePage
from page_objects.login_page import LoginPage


class AccountPage(BasePage):
    """Page object for Account Page on Automation Test Store."""

    # URLS
    ACCOUNT_PAGE_URL = 'https://automationteststore.com/index.php?rt=account/account'

    # INITIALIZER
    def __init__(self, driver):
        super().__init__(driver)

    # INTERACTIONS
    def url_return(self):
        return self.ACCOUNT_PAGE_URL

    # VALIDATIONS
    def check_if_logged_in(self, driver):
        super().go_to_url(self.ACCOUNT_PAGE_URL)
        if driver.current_url == self.url_return():
            return True
        else:
            return False
