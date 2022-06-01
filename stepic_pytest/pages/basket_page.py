from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def should_be_message_about_empty_basket(self):
        message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert "empty" in message, "There should be a message about empty basket"

    def should_not_be_basket_items_in_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "There should not be basket items in empty basket"

    def should_be_basket_items_in_basket_after_adding_product(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_ITEMS), "There should be basket items after adding product"
