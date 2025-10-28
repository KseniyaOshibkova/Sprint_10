import allure

from locators.preparing_to_order_taxi_locators import PreparingToOrderTaxiLocators
from pages.base_page import BasePage


class PreparingToOrderTaxiPage(BasePage):

    @allure.step("Выбор режима маршрута 'Оптимальный'")
    def select_optimal_route_mode(self):
        self.click_element(PreparingToOrderTaxiLocators.OPTIMAL_MODE)


    @allure.step("Выбор режима маршрута 'Быстрый'")
    def select_fast_route_mode(self):
        self.click_element(PreparingToOrderTaxiLocators.FAST_MODE)


    @allure.step("Выбор режима маршрута 'Свой'")
    def select_custom_route_mode(self):
        self.click_element(PreparingToOrderTaxiLocators.SVOY_MODE)

    def check_active_route_mode(self, expected_mode_text):
        active_text = self.get_text_from_element(PreparingToOrderTaxiLocators.MODE_ACTIVE)
        assert expected_mode_text in active_text, (
            f"Ожидался активный режим '{expected_mode_text}', а найден '{active_text}'")

    @allure.step("Проверка изменения стоимости и длительности маршрута")
    def check_route_price_and_duration_changed(self, old_price, old_duration):
        """Проверяет, что стоимость и длительность маршрута реально изменились"""
        new_price = self.wait_for_text_change(PreparingToOrderTaxiLocators.PRICE, old_price)
        new_duration = self.wait_for_text_change(PreparingToOrderTaxiLocators.DURATION, old_duration)
        assert new_price != old_price, f"Стоимость маршрута не изменилась, осталось '{old_price}'"
        assert new_duration != old_duration, f"Длительность маршрута не изменилась, осталось '{old_duration}'"


    @allure.step("Проверка активности кнопки вызова или бронирования такси")
    def check_active_button(self, button_name):
        button = self.find_element(button_name)
        assert button.is_enabled(), "Кнопка вызова или бронирования неактивна"


    @allure.step("Проверка активации всех типов передвижения в режиме 'Свой'")
    def check_all_move_types_active(self):
        """Проверяет, что активны все типы передвижения: Машина, Пешком, Такси, Велосипед, Самокат, Драйв"""
        elements = self.find_elements(PreparingToOrderTaxiLocators.TYPES_ACTIVE)
        expected_count = 6
        assert len(elements) == expected_count, (
            f"Ожидалось {expected_count} активных типов передвижения, а найдено {len(elements)}")


    @allure.step("Выбор типа передвижения 'Драйв'")
    def select_drive_move_type(self):
        self.click_element(PreparingToOrderTaxiLocators.SVOY_MODE_TYPE_DRIVE)

    @allure.step("Переключение между 'Быстрый' и 'Оптимальный' и проверка пересчета стоимости/времени")
    def switch_between_fast_and_optimal_and_check_recalculation(self):
        container = self.waiting_for_element(PreparingToOrderTaxiLocators.RESULTS_CONTAINER)

        # Сохраняем старые значения
        old_price = container.find_element(*PreparingToOrderTaxiLocators.PRICE).text
        old_duration = container.find_element(*PreparingToOrderTaxiLocators.DURATION).text

        # Переключаемся на 'Оптимальный'
        self.select_optimal_route_mode()

        # Проверяем, что активный таб сменился
        self.check_active_route_mode("Оптимальный")

        # Берём новые значения сразу
        new_price = container.find_element(*PreparingToOrderTaxiLocators.PRICE).text
        new_duration = container.find_element(*PreparingToOrderTaxiLocators.DURATION).text

        # Проверяем, что они реально изменились
        assert new_price != old_price, f"Стоимость маршрута не изменилась: {old_price}"
        assert new_duration != old_duration, f"Длительность маршрута не изменилась: {old_duration}"


    @allure.step("Проверка активации типов передвижения при выборе режима 'Свой'")
    def check_move_types_activation_on_custom_mode(self):
        self.select_custom_route_mode()
        self.check_all_move_types_active()


    @allure.step("Проверка активности кнопки 'Вызвать такси' при режиме 'Быстрый'")
    def check_call_taxi_button_active_on_fast_mode(self):
        self.select_fast_route_mode()
        self.waiting_for_element(PreparingToOrderTaxiLocators.ORDER_TAXI_BUTTON)
        self.check_active_button(PreparingToOrderTaxiLocators.ORDER_TAXI_BUTTON)


    @allure.step("Проверка активности кнопки 'Забронировать' при выборе 'Свой' и типа 'Драйв'")
    def check_booking_button_active_on_custom_drive(self):
        self.select_custom_route_mode()
        self.waiting_for_element(PreparingToOrderTaxiLocators.SVOY_MODE_TYPE_DRIVE)
        self.select_drive_move_type()
        self.wait_for_element_to_be_clickable(PreparingToOrderTaxiLocators.ORDER_BUTTON)
