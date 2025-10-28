import allure
import pytest


@allure.feature("Подготовка к заказу такси")
class TestPreparingToOrderTaxi:

    @allure.title("Смена активного таба между 'Оптимальный' и 'Быстрый' и пересчет стоимости/времени")
    @pytest.mark.xfail(reason="Время в пути при переключении тарифов не меняется")
    def test_switch_optimal_fast_route_recalculation(self, driver, drawing_route_page, preparing_to_order_taxi_page):
        drawing_route_page.input_different_point()
        preparing_to_order_taxi_page.switch_between_fast_and_optimal_and_check_recalculation()

    @allure.title("Активация типов передвижения при выборе режима 'Свой'")
    def test_custom_mode_activates_move_types(self, driver, drawing_route_page, preparing_to_order_taxi_page):
        drawing_route_page.input_different_point()
        preparing_to_order_taxi_page.check_move_types_activation_on_custom_mode()

    @allure.title("Активность кнопки 'Вызвать такси' при режиме 'Быстрый'")
    def test_fast_mode_call_taxi_button_active(self,  driver, drawing_route_page, preparing_to_order_taxi_page):
        drawing_route_page.input_different_point()
        preparing_to_order_taxi_page.check_call_taxi_button_active_on_fast_mode()

    @allure.title("Активность кнопки 'Забронировать' при режиме 'Свой' и типе 'Драйв'")
    def test_custom_mode_drive_booking_button(self,  driver, drawing_route_page, preparing_to_order_taxi_page):
        drawing_route_page.input_different_point()
        preparing_to_order_taxi_page.check_booking_button_active_on_custom_drive()
