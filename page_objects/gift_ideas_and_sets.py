# IMPORTS

from page_objects.base_page import BasePage

from selenium.webdriver.common.by import By


class GiftIdeasAndSetsPage(BasePage):
    """Page object for Account Page on Automation Test Store."""

    # URLS
    GIFT_IDEAS_AND_SETS_URL = 'https://automationteststore.com/index.php?rt=product/category&path=43_45'

    # LOCATORS
    NIGHT_CARE_CREMA_LINK = (By.XPATH, '//title="Night Care Crema Nera Obsidian Mineral Complex"')

    # INITIALIZER
    def __init__(self, driver):
        super().__init__(driver)

    # INTERACTIONS
    def url_return(self):
        return self.GIFT_IDEAS_AND_SETS_URL

    def go_to_night_care_crema(self):
        super().click(self.NIGHT_CARE_CREMA_LINK)
