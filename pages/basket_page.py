from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_empty_basket(self):
        """ Проверяем, что корзина пуста (нет товаров) """
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Корзина не пуста!"

    def should_have_empty_basket_text(self):
        """ Проверяем, что есть текст о пустой корзине """
        empty_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text
        assert "Your basket is empty" in empty_text, "Нет сообщения, что корзина пуста!"