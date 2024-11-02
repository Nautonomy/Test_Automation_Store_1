# IMPORTS

from page_objects.base_page import BasePage
from page_objects.login_page import LoginPage

from selenium.webdriver.common.by import By


class CartPage(BasePage):
    """Page object for Cart Page on Automation Test Store."""

    # URLS
    CART_PAGE_URL = 'https://automationteststore.com/index.php?rt=checkout/cart'

    # LOCATORS
    CHECKOUT_BUTTON = (By.ID, 'cart_checkout1')

    # INITIALIZER
    def __init__(self, driver):
        super().__init__(driver)

    # INTERACTIONS
    def url_return(self):
        return self.CART_PAGE_URL

    def checkout(self):
        super().click(self.CHECKOUT_BUTTON)
