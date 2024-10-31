# IMPORTS
from page_objects.base_page import BasePage


class CreateAccountSuccessPage(BasePage):
    """Page object for Successful Create Account Page on Automation Test Store."""

    # URLS
    CREATE_ACCOUNT_SUCCESS_PAGE_URL = 'https://automationteststore.com/index.php?rt=account/success'

    # INITIALIZER
    def __init__(self, driver):
        super().__init__(driver)

    # INTERACTIONS
    def url_return(self):
        return self.CREATE_ACCOUNT_SUCCESS_PAGE_URL
