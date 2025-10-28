import allure

from locators.drawing_route_locators import DrawingRouteLocators
from locators.drawing_route_with_selection_locators import DrawingRouteWithSelectionLocators
import data
from locators.preparing_to_order_taxi_locators import PreparingToOrderTaxiLocators
from pages.base_page import BasePage


class DrawingRouteWithSelectionPage(BasePage):

    @allure.step('Ввод разных адресов откуда/куда')
    def input_different_point(self):
        self.fill_input(DrawingRouteLocators.FROM_INPUT, data.ADDRESS1)
        self.fill_input(DrawingRouteLocators.TO_INPUT, data.ADDRESS2)


    @allure.step('Ввод одинаковых адресов откуда/куда')
    def input_equal_point(self):
        self.fill_input(DrawingRouteLocators.FROM_INPUT, data.ADDRESS1)
        self.fill_input(DrawingRouteLocators.TO_INPUT, data.ADDRESS1)


    @allure.step('Проверить, что блок выбора маршрута отображается')
    def check_route_block_displayed(self):
        assert self.check_displayed_element(DrawingRouteWithSelectionLocators.BLOCK_ROUTE), \
            "Блок выбора маршрута не отображается"


    @allure.step('Проверить, что выбран режим "Оптимальный"')
    def check_optimal_mode(self):
        assert self.check_displayed_element(PreparingToOrderTaxiLocators.OPTIMAL_MODE), \
            'Режим "Оптимальный" не отображается'


    @allure.step('Проверить, что отображается текст "Авто Бесплатно" и "В пути 0 мин."')
    def check_equal_route_text(self):
        price_text = self.get_text_from_element(DrawingRouteWithSelectionLocators.PRICE)
        duration_text = self.get_text_from_element(DrawingRouteWithSelectionLocators.DURATION)
        assert data.EQUAL_ROUTE_TEXT in price_text, (f"Ожидался текст '{data.EQUAL_ROUTE_TEXT}', а получен"
                                                     f" '{price_text}'")
        assert data.EQUAL_ROUTE_DURATION in duration_text, (f"Ожидался текст '{data.EQUAL_ROUTE_DURATION}', а получен"
                                                            f" '{duration_text}'")


    @allure.step('Проверить отрисовку блока выбора маршрута при вводе разных адресов')
    def drawing_route_block_different_address(self):
        self.input_different_point()
        self.check_route_block_displayed()
        self.check_optimal_mode()


    @allure.step('Проверить отрисовку блока выбора маршрута при вводе одинаковых адресов')
    def drawing_route_block_equal_address(self):
        self.input_equal_point()
        self.check_route_block_displayed()
        self.check_equal_route_text()
