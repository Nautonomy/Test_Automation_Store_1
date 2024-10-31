# IMPORTS
import time
import keyring

from selenium.webdriver.common.by import By
from faker import Faker

from page_objects.base_page import BasePage


class CreateAccountPage(BasePage):
    """Page object for Create Account Page on Automation Test Store."""

    # URLS
    CREATE_ACCOUNT_PAGE_URL = 'https://automationteststore.com/index.php?rt=account/create'

    # LOCATORS
    account_create_firstname = (By.ID, 'AccountFrm_firstname')
    account_create_lastname = (By.ID, 'AccountFrm_lastname')
    account_create_email = (By.ID, 'AccountFrm_email')
    account_create_telephone = (By.ID, 'AccountFrm_telephone')
    account_create_fax = (By.ID, 'AccountFrm_fax')
    account_create_company = (By.ID, 'AccountFrm_company')
    account_create_address_1 = (By.ID, 'AccountFrm_address_1')
    account_create_address_2 = (By.ID, 'AccountFrm_address_2')
    account_create_city = (By.ID, 'AccountFrm_city')
    account_create_zone_id = (By.ID, 'AccountFrm_zone_id')
    account_create_postcode = (By.ID, 'AccountFrm_postcode')
    account_create_country_id = (By.ID, 'AccountFrm_country_id')
    account_create_loginname = (By.ID, 'AccountFrm_loginname')
    account_create_password = (By.ID, 'AccountFrm_password')
    account_create_confirm = (By.ID, 'AccountFrm_confirm')
    account_create_newsletter0 = (By.ID, 'AccountFrm_newsletter0')
    account_create_AccountFrm_agree = (By.ID, 'AccountFrm_agree')
    account_create_Continue_button = (By.XPATH, "//button[@title='Continue']")

    account_create_failure_message = (By.CLASS_NAME, 'alert alert-error alert-danger')

    # INITIALIZER
    def __init__(self, driver):
        super().__init__(driver)

    # INTERACTIONS
    fake = Faker()
    registered_login = ""
    registered_password = ""

    def fill_in_form_correct(self):
        super().text(self.account_create_firstname, self.fake.first_name())
        super().text(self.account_create_lastname, self.fake.last_name())
        super().text(self.account_create_email, self.fake.email())
        super().text(self.account_create_address_1, self.fake.address())
        super().text(self.account_create_city, self.fake.city())
        super().text(self.account_create_postcode, self.fake.zipcode())
        registered_login = self.fake.user_name()
        keyring.set_password("TATS1_id", "TATS1_registered_login", registered_login)
        super().text(self.account_create_loginname, registered_login)
        registered_password = self.fake.password()
        keyring.set_password("TATS1_id", "TATS1_registered_password", registered_password)
        super().text(self.account_create_password, registered_password)
        super().text(self.account_create_confirm, registered_password)
        country = super().random_item_from_dropdown_list(self.account_create_country_id)
        super().dropdown_selection_by_text(self.account_create_country_id, country)
        time.sleep(1)
        zone = super().random_item_from_dropdown_list(self.account_create_zone_id)
        super().dropdown_selection_by_text(self.account_create_zone_id, zone)
        super().click(self.account_create_newsletter0)
        super().click(self.account_create_AccountFrm_agree)

    def fill_in_form_incorrect(self):
        super().text(self.account_create_lastname, self.fake.last_name())
        super().text(self.account_create_email, self.fake.email())
        super().text(self.account_create_address_1, self.fake.address())
        super().text(self.account_create_city, self.fake.city())
        super().text(self.account_create_postcode, self.fake.zipcode())
        super().text(self.account_create_loginname, self.fake.user_name())
        pw = self.fake.password()
        super().text(self.account_create_password, pw)
        super().text(self.account_create_confirm, pw)
        country = super().random_item_from_dropdown_list(self.account_create_country_id)
        super().dropdown_selection_by_text(self.account_create_country_id, country)
        time.sleep(1)
        zone = super().random_item_from_dropdown_list(self.account_create_zone_id)
        super().dropdown_selection_by_text(self.account_create_zone_id, zone)
        super().click(self.account_create_newsletter0)
        super().click(self.account_create_AccountFrm_agree)

    def click_continue_button(self):
        super().click(self.account_create_Continue_button)

    def error_message_visible(self):
        return super().check_if_element_is_visible(self.account_create_failure_message)

    def url_return(self):
        return self.CREATE_ACCOUNT_PAGE_URL

