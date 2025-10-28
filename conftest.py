import allure
import pytest
from selenium import webdriver

import data
from pages.drawing_route_with_selection_page import DrawingRouteWithSelectionPage
from pages.preparing_to_order_taxi_page import PreparingToOrderTaxiPage
from pages.order_taxi_page import OrderTaxiPage
from pages.drawing_route_page import DrawingRoutePage


@pytest.fixture
def driver():
    # Фикстура создает экземпляр класса для каждого теста, открывает главную страницу, закрывает браузер
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(data.BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture(scope='function', autouse=False)
def drawing_route_page(driver):
    return DrawingRoutePage(driver)

@pytest.fixture(scope='function', autouse=False)
def order_taxi_page(driver):
    return OrderTaxiPage(driver)

@pytest.fixture(scope='function', autouse=False)
def preparing_to_order_taxi_page(driver):
    return PreparingToOrderTaxiPage(driver)

@pytest.fixture(scope='function', autouse=False)
def drawing_route_with_selection_page(driver):
    return DrawingRouteWithSelectionPage(driver)

@pytest.fixture
def prepared_order_taxi_page(drawing_route_with_selection_page, order_taxi_page):
    """Фикстура, которая подготавливает маршрут и вызывает такси"""
    with allure.step("Подготовка маршрута для вызова такси"):
        with allure.step("Вводим разные адреса в поля 'Откуда' и 'Куда'"):
            drawing_route_with_selection_page.input_different_point()

        with allure.step("Выбираем быстрый маршрут"):
            order_taxi_page.select_fast_route()

        with allure.step("Нажимаем кнопку 'Вызвать такси'"):
            order_taxi_page.click_order_taxi_button()

    return order_taxi_page
