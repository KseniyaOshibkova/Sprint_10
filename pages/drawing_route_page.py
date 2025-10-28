import allure

import data
from locators.drawing_route_locators import DrawingRouteLocators
from pages.base_page import BasePage


class DrawingRoutePage(BasePage):

    @allure.step('Ввод разных адресов откуда/куда')
    def input_different_point(self):
        # точка откуда
        self.fill_input(DrawingRouteLocators.FROM_INPUT, data.ADDRESS1)
        # точка куда
        self.fill_input(DrawingRouteLocators.TO_INPUT, data.ADDRESS2)

    @allure.step('Ввод одинаковых адресов откуда/куда')
    def input_equal_point(self):
        self.fill_input(DrawingRouteLocators.FROM_INPUT, data.ADDRESS1)
        self.fill_input(DrawingRouteLocators.TO_INPUT, data.ADDRESS1)

    @allure.step('Проверить отрисовку маршрута при вводе разных адресов')
    def drawing_route_different_address(self):
        self.input_different_point()
        assert self.check_displayed_element(DrawingRouteLocators.ROUTE_POINT_A), \
            "Не найдена первая точка маршрута (A)"
        assert self.check_displayed_element(DrawingRouteLocators.ROUTE_POINT_B), \
            "Не найдена вторая точка маршрута (B)"
