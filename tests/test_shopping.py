# IMPORTS
import time

import pytest

from page_objects.home_page import HomePage
from page_objects.login_page import LoginPage
from page_objects.account_page import AccountPage
from page_objects.gift_ideas_and_sets import GiftIdeasAndSetsPage
from page_objects.the_product_page import NightCareCremaPage
from page_objects.cart_page import CartPage
from page_objects.checkout import CheckoutPage
from page_objects.checkout_success import CheckoutSuccessPage


# TESTS
class TestShopping:

    def test_buy_product_via_browsing(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        gift_ideas_and_sets = GiftIdeasAndSetsPage(driver)
        night_care_crema_page = NightCareCremaPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)
        checkout_success_page = CheckoutSuccessPage(driver)

        home_page.go_to_home_page()
        home_page.go_to_gift_ideas_and_sets()
        assert driver.current_url == GiftIdeasAndSetsPage.url_return, "Current url is different than expected."
        gift_ideas_and_sets.go_to_night_care_crema()
        assert driver.current_url == night_care_crema_page.url_browsing_return(), ("Current url is different than "
                                                                                   "expected.")
        night_care_crema_page.add_night_care_crema_to_cart()
        assert driver.current_url == cart_page.url_return()
        cart_page.checkout()
        if driver.current_url == login_page.url_return():
            login_page.fill_login_form_correct()
        assert driver.current_url == checkout_page.url_return(), "Current url is different than expected."
        checkout_page.confirm_order()
        assert driver.current_url == checkout_success_page.url_return(), "Current url is different than expected."

    @pytest.mark.current
    def test_buy_product_via_searching(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        night_care_crema_page = NightCareCremaPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)
        checkout_success_page = CheckoutSuccessPage(driver)

        home_page.go_to_home_page()
        home_page.search_for_night_care_crema()
        assert driver.current_url == night_care_crema_page.url_return(), "Current url is different than expected."
        night_care_crema_page.add_night_care_crema_to_cart()
        assert driver.current_url == cart_page.url_return()
        cart_page.checkout()
        if driver.current_url == login_page.url_return():
            login_page.fill_login_form_correct()
        assert driver.current_url == checkout_page.url_return(), "Current url is different than expected."
        checkout_page.confirm_order()
        time.sleep(1)
        assert driver.current_url == checkout_success_page.url_return(), "Current url is different than expected."
