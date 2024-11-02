# IMPORTS
import pytest

from page_objects.home_page import HomePage
from page_objects.login_page import LoginPage
from page_objects.create_account_page import CreateAccountPage
from page_objects.create_account_success_page import CreateAccountSuccessPage
from page_objects.account_page import AccountPage


# TESTS
class TestAccountCreation:

    @pytest.mark.current
    def test_correct_form_fill(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        create_account_page = CreateAccountPage(driver)
        create_account_success_page = CreateAccountSuccessPage(driver)

        home_page.go_to_home_page()
        home_page.go_to_login_page()
        login_page.go_to_create_account_page()
        create_account_page.fill_in_form_correct()
        create_account_page.click_continue_button()
        assert driver.current_url == create_account_success_page.url_return(), "Current url is different than expected."

    def test_incorrect_form_fill(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        create_account_page = CreateAccountPage(driver)

        home_page.go_to_home_page()
        home_page.go_to_login_page()
        login_page.go_to_create_account_page()
        create_account_page.fill_in_form_incorrect()
        create_account_page.click_continue_button()
        assert create_account_page.error_message_visible(), "Error message does not appear."


class TestLogin:

    def test_login_correct(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        account_page = AccountPage(driver)

        home_page.go_to_home_page()
        home_page.go_to_login_page()
        login_page.fill_login_form_correct()
        assert driver.current_url == account_page.url_return(), "Current url is different than expected."

    def test_login_incorrect(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)

        home_page.go_to_home_page()
        home_page.go_to_login_page()
        login_page.fill_login_form_incorrect()
        assert login_page.error_message_visible(), "Error message does not appear."
