import time

import pytest

from StepicSeleniumProject.pages.basket_page import BasketPage
from StepicSeleniumProject.pages.login_page import LoginPage
from StepicSeleniumProject.pages.product_page import ProductPage


@pytest.mark.userbasketfixtures
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.browser = browser
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        loginpage = LoginPage(self.browser, link)
        loginpage.open()
        email = str(time.time()) + "@fakemail.org"
        password = "gfdsa12345"
        loginpage.register_new_user(email, password)
        loginpage.should_be_authorized_user()

    @pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                              pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
                                           "/?promo=offer7", marks=pytest.mark.xfail),
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    def test_user_can_add_product_to_basket(self, link):
        # Get to page
        page = ProductPage(self.browser, link)
        page.open()
        page.should_be_authorized_user()
        # CLick add to cart
        page.product_add_to_cart()
        page.solve_quiz_and_get_code()
        # check that was added
        page.product_should_be_added_to_cart()

    def test_user_cant_see_success_message(self):
        # 1 open page
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(self.browser, link)
        page.open()
        page.should_be_authorized_user()
        # 2 no message by using 'is_not_element_present'
        page.should_not_be_success_message()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
                                               "/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    # Get to page
    page = ProductPage(browser, link)
    page.open()
    # CLick add to cart
    page.product_add_to_cart()
    page.solve_quiz_and_get_code()
    # check that was added
    page.product_should_be_added_to_cart()


def test_guest_cant_see_success_message(browser):
    # 1 open page
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    # 2 no message by using 'is_not_element_present'
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # 1 open page
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    # 2 add good to cart
    page.product_add_to_cart()
    # 3 no message by using 'is_not_element_present'
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    # 1 open page
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    # 2 add to cart
    page.product_add_to_cart()
    # 3 no success message with 'is_disappeared'
    page.success_message_should_dissapear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # 1 open page with product
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    # 2 go to basket page through header
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    # 3 basket should not have products
    basket_page.basket_should_not_have_items()
    # 4 basket should have message about emptiness
    basket_page.empty_basket_should_have_message()
