# IMPORTS

from page_objects.base_page import BasePage

from selenium.webdriver.common.by import By


class CheckoutPage(BasePage):
    """Page object for Checkout Page on Automation Test Store."""

    # URLS
    CHECKOUT_URL = 'https://automationteststore.com/index.php?rt=checkout/confirm'

    # LOCATORS
    CONFIRM_ORDER_BUTTON = (By.ID, 'checkout_btn')

    # INITIALIZER
    def __init__(self, driver):
        super().__init__(driver)

    # INTERACTIONS
    def url_return(self):
        return self.CHECKOUT_URL

    def confirm_order(self):
        super().click(self.CONFIRM_ORDER_BUTTON)
