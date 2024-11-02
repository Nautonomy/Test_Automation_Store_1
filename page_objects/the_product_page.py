# IMPORTS

from page_objects.base_page import BasePage

from selenium.webdriver.common.by import By


class NightCareCremaPage(BasePage):
    """Page object for The Night Care Crema Nera Obsidian Mineral Complex Page on Automation Test Store."""

    # URLS
    NIGHT_CARE_CREMA_BROWSING_URL = ('https://automationteststore.com/index.php?rt=product/product&path=43_45'
                                     '&product_id=94')
    NIGHT_CARE_CREMA_URL = 'https://automationteststore.com/index.php?rt=product/product&product_id=94'

    # LOCATORS
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, 'cart')

    # INITIALIZER
    def __init__(self, driver):
        super().__init__(driver)

    # INTERACTIONS
    def url_return(self):
        return self.NIGHT_CARE_CREMA_URL

    def url_browsing_return(self):
        return self.NIGHT_CARE_CREMA_BROWSING_URL

    def add_night_care_crema_to_cart(self):
        super().click(self.ADD_TO_CART_BUTTON)
