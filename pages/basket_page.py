from StepicSeleniumProject.pages.base_page import BasePage
from StepicSeleniumProject.pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        url = self.browser.current_url
        assert "/basket" in url, f"Page should contain 'basket' but it is '{url}'"

    def empty_basket_should_have_message(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_EMPTY_MESSAGE), f"message should be present for empty basket"

    def full_basket_should_not_have_message(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_EMPTY_MESSAGE), "When basket is filled there should not be message that it's empty"

    def basket_should_have_items(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ELEMENTS_SELECTOR), "Basket should have elements in it"

    def basket_should_not_have_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ELEMENTS_SELECTOR), "Empty basket should not " \
                                                                                          "have elements "
