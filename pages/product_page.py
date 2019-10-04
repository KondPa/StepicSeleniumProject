from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product(self):
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_ADD_TO_CART_BUTTON), "Product add to cart button is missing"

    def product_add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_TO_CART_BUTTON)
        button.click()

    def product_should_be_added_to_cart(self):
        number = self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET_ALERT).text
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        added_name = self.browser.find_element(*ProductPageLocators.PRODUCT_ALERT_NAME_OF_ADDED_GOOD).text
        assert str(name) == str(added_name), f"Name '{name}' should be equal to '{added_name}'"
        assert number == price, f"Price '{price}' should be equal to '{number}'"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ALERT_NAME_OF_ADDED_GOOD), \
            "Success message is presented, but should not be"

    def success_message_should_dissapear(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_ALERT_NAME_OF_ADDED_GOOD), \
            "Success message is presented, but should have disapeared"
