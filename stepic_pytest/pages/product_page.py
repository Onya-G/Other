from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BASKET_BUTTON).click()

    def should_be_message_about_adding_product(self):
        assert self.is_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Product addition message does't appear"

    def should_be_message_about_basket_total_sum(self):
        assert self.is_element_present(
            *ProductPageLocators.BASKET_MESSAGE), "Basket total sum message does't appear"

    def product_name_should_be_in_message(self):
        prod_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert prod_name in message, "Product name should be in message"

    def basket_total_should_be_equal_product_price(self):
        prod_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        message = self.browser.find_element(*ProductPageLocators.BASKET_MESSAGE).text
        assert prod_price == message, "Basket total sum should be equal product price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message doesn't disappear"


