from .locators import ProductPageLocators
from .base_page import BasePage

class ProductPage(BasePage):
    # Добавление товара в корзину
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    # Получаем название продукта
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    # Получаем цену продукта
    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Сообщение об успехе отображается, но не должно"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Сообщение об успехе не исчезло"

    # Проверка добавления товара в корзину
    def check_product_added_successfully(self, expected_name):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Нет сообщения об успешном добавлении товара"
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert expected_name == success_message, f"Ожидали '{expected_name}', а получили '{success_message}'"

    # Проверка цены с добавленным товаром
    def check_basket_price(self, expected_price):
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert expected_price in basket_total, f"Ожидали цену '{expected_price}', а получили '{basket_total}'"
