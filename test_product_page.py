import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

promos = ["offer0", "offer1", "offer2",
          "offer3", "offer4", "offer5",
          "offer6", pytest.param("offer7", marks=pytest.mark.xfail), "offer8",
          "offer9"]
@pytest.mark.parametrize('promo', promos)
def test_guest_can_add_product_to_basket(browser, promo):
    """Проверяем, что гость может правильно добавить товар в корзину"""
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promo}'
    page = ProductPage(browser, link)
    page.open()
    product_name = page.get_product_name()
    product_price = page.get_product_price()

    page.add_to_basket()
    page.solve_quiz_and_get_code()

    page.check_product_added_successfully(product_name)
    page.check_basket_price(product_price)

@pytest.mark.xfail(reason="Сообщение об успехе отображается после добавления товара")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """ Проверяем, что после добавления товара НЕТ сообщения об успехе """
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    """ Проверяем, что сообщение об успехе НЕ отображается на странице товара до его добавления """
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="Сообщение об успехе не исчезает")
def test_message_disappeared_after_adding_product_to_basket(browser):
    """ Проверяем, что сообщение об успехе исчезает после добавления товара в корзину """
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.success_message_should_disappear()

def test_guest_should_see_login_link_on_product_page(browser):
    """ Проверяем, что гость может увидеть ссылку для входа на странице товара """
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    """ Проверяем, что гость может перейти на страницу логина со страницы товара """
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """ Гость не видит товары в корзине, если перешел в неё со страницы товара """
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_have_empty_basket_text()
