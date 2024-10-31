# IMPORTS

from page_objects.base_page import BasePage


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
