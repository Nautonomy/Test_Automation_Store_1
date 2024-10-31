# IMPORTS
import keyring

from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class LoginPage(BasePage):
    """Page object for Login Page on Automation Test Store."""

    # URLS
    LOGIN_PAGE_URL = 'https://automationteststore.com/index.php?rt=account/login'

    # Locators

    register_account_button = (By.XPATH, "//button[@title='Continue']")
    login_loginname = (By.ID, 'loginFrm_loginname')
    login_password = (By.ID, 'loginFrm_password')
    login_button = (By.XPATH, "//button[@title='Login']")
    login_failure_message = (By.CLASS_NAME, "alert alert-error alert-danger")

    # INITIALIZER
    def __init__(self, driver):
        super().__init__(driver)

    registered_login = ""
    registered_password = ""

    # INTERACTIONS
    def go_to_create_account_page(self):
        super().click(self.register_account_button)

    def fill_login_form_correct(self):
        login = keyring.get_password("TATS1_id", "TATS1_registered_login")
        super().text(self.login_loginname, login)
        password = keyring.get_password("TATS1_id", "TATS1_registered_password")
        super().text(self.login_password, password)
        super().click(self.login_button)

    def fill_login_form_incorrect(self):
        login = keyring.get_password("TATS1_id", "TATS1_registered_login")
        super().text(self.login_loginname, login)
        password = keyring.get_password("TATS1_id", "TATS1_registered_password")+"1"
        super().text(self.login_password, password)
        super().click(self.login_button)

    def error_message_visible(self):
        return super().check_if_element_is_visible(self.login_failure_message)
