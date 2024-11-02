# IMPORTS

from page_objects.base_page import BasePage


class CheckoutSuccessPage(BasePage):
    """Page object for Checkout Success Page on Automation Test Store."""

    # URLS
    CHECKOUT_SUCCESS_URL = 'https://automationteststore.com/index.php?rt=checkout/success'

    # INITIALIZER
    def __init__(self, driver):
        super().__init__(driver)

    # INTERACTIONS
    def url_return(self):
        return self.CHECKOUT_SUCCESS_URL

