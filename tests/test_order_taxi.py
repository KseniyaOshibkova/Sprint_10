import pytest
import allure
import data

class TestOrderTaxi:

    @allure.title("Проверка отображения всех тарифов и активного тарифа")
    def test_all_fares_displayed(self, driver, prepared_order_taxi_page):
        prepared_order_taxi_page.verify_all_fares_displayed()
        prepared_order_taxi_page.verify_active_fare_displayed()

    @allure.title("Проверка описания тарифов при наведении на иконку i")
    @pytest.mark.xfail(reason="Перепутаны описания тарифов")
    @pytest.mark.parametrize("fare_name, expected_description", data.RATES)
    def test_fares_tooltip_descriptions(self, driver, prepared_order_taxi_page, fare_name, expected_description):
        prepared_order_taxi_page.select_fare_by_name(fare_name)
        actual_description = prepared_order_taxi_page.hover_fare_info_icon_by_name(fare_name)
        assert actual_description == expected_description, (
            f"Описание тарифа '{fare_name}' некорректно: ожидалось '{expected_description}', "
            f"получено '{actual_description}'")

    @allure.title("Проверка отображения блока заказа под тарифами")
    def test_order_fields_displayed(self, driver, prepared_order_taxi_page):
        prepared_order_taxi_page.verify_phone_field_displayed()
        prepared_order_taxi_page.verify_payment_field_displayed()
        prepared_order_taxi_page.verify_comment_field_displayed()
        prepared_order_taxi_page.verify_requirements_field_displayed()


    @allure.title("Полный флоу заказа тарифа 'Рабочий' с чекбоксом и деталями")
    @pytest.mark.xfail(reason="Кнопка 'Отменить' в окне Заказа такси не работает")
    def test_complete_order_flow(self, driver, prepared_order_taxi_page):
        page = prepared_order_taxi_page

        with allure.step("Выбираем тариф 'Рабочий' и сохраняем его цену"):
            page.select_working_fare()
            expected_price = page.get_selected_fare_price(data.WORKING)

        with allure.step("Включаем чекбокс 'Столик для ноутбука'"):
            page.open_order_requirements()
            page.enable_table_for_notebook()

        with allure.step("Нажимаем кнопку 'Вызвать такси'"):
            page.click_order_taxi_smart_button()

        with allure.step("Проверяем отображение окна ожидания машины"):
            page.verify_wait_car_window_displayed()

        with allure.step("Дожидаемся завершения поиска машины и проверяем окно совершенного заказа"):
            page.verify_completed_order_window_displayed()

        with allure.step("Нажимаем кнопку 'Детали' и проверяем стоимость тарифа"):
            page.click_details_button()
            page.verify_price_in_details(expected_price)

        with allure.step("Нажимаем кнопку 'Отменить' для закрытия заказа"):
            page.cancel_order()
