import allure
from pages.base_page import BasePage
from locators.order_taxi_locators import OrderTaxiLocators
import data

class OrderTaxiPage(BasePage):

    @allure.step("Выбрать маршрут 'Быстрый'")
    def select_fast_route(self):
        self.click_element(OrderTaxiLocators.ROUTE_TYPE_FAST)

    @allure.step(f"Нажать кнопку '{data.TEXT_TYPE_FAST}'")
    def click_order_taxi_button(self):
        self.click_element(OrderTaxiLocators.ORDER_TAXI_BUTTON)

    @allure.step(f"Нажать кнопку Ввести номер и заказать")
    def click_order_taxi_smart_button(self):
        self.click_element(OrderTaxiLocators.SMART_BUTTON)

    @allure.step("Проверить, что все тарифы отображаются")
    def verify_all_fares_displayed(self):
        fares = self.find_elements(OrderTaxiLocators.FARE_CARDS)
        assert len(fares) == len(data.RATE_TYPE_LIST), \
            f"Ожидалось {len(data.RATE_TYPE_LIST)} тарифов, найдено {len(fares)}"

    @allure.step("Проверить, что активный тариф отображается")
    def verify_active_fare_displayed(self):
        active = self.find_element(OrderTaxiLocators.ACTIVE_ROUTE_TYPE)
        assert active.is_displayed(), "Активный тариф не отображается"

    @allure.step("Получить все элементы тарифов")
    def get_all_fares_elements(self):
        return self.find_elements(OrderTaxiLocators.FARE_CARDS)

    @allure.step("Выбрать тариф '{fare_name}'")
    def select_fare_by_name(self, fare_name):
        fares = self.get_all_fares_elements()
        for fare in fares:
            title = fare.find_element(*OrderTaxiLocators.FARE_TITLE).text
            if title == fare_name:
                fare.click()
                return
        raise ValueError(f"Тариф с названием '{fare_name}' не найден")

    @allure.step("Выбрать тариф 'Рабочий'")
    def select_working_fare(self):
        fare = self.find_element(OrderTaxiLocators.FARE_WORK)
        fare.click()

    @allure.step("Навести на иконку информации тарифа '{fare_name}' и вернуть описание")
    def hover_fare_info_icon_by_name(self, fare_name):
        fares = self.get_all_fares_elements()
        for fare in fares:
            title = fare.find_element(*OrderTaxiLocators.FARE_TITLE).text
            if title == fare_name:
                info_button = fare.find_element(*OrderTaxiLocators.FARE_INFO_BUTTON)
                self.move_to_element(info_button)
                description = fare.find_element(*OrderTaxiLocators.TESTING_HOVER_FARE_DESCRIPTION).text
                return description
        raise ValueError(f"Тариф с названием '{fare_name}' не найден")


    @allure.step("Проверить отображение поля '{field_name}'")
    def verify_field_displayed(self, locator, field_name):
        element = self.find_element(locator)
        assert element.is_displayed(), f"Поле '{field_name}' не отображается"

    def verify_phone_field_displayed(self):
        self.verify_field_displayed(OrderTaxiLocators.PHONE_FIELD, data.CUST_PHONE)

    def verify_payment_field_displayed(self):
        self.verify_field_displayed(OrderTaxiLocators.PAYMENT_FIELD, data.PAY_METHOD)

    def verify_comment_field_displayed(self):
        self.verify_field_displayed(OrderTaxiLocators.COMMENT_FIELD, data.DRIVER_COMMENT)

    def verify_requirements_field_displayed(self):
        self.verify_field_displayed(OrderTaxiLocators.REQUIREMENTS_FIELD, data.ORDER_REQUIREMENTS)

    @allure.step("Открыть Требования к заказу")
    def open_order_requirements(self):
        select = self.find_element(OrderTaxiLocators.REQUIREMENTS_FIELD)
        select.click()


    @allure.step("Включить чекбокс 'Столик для ноутбука'")
    def enable_table_for_notebook(self):
        checkbox = self.find_element(OrderTaxiLocators.CHECKBOX_TABLE_FOR_NOTEBOOK)
        if not checkbox.is_selected():
            checkbox.click()


    @allure.step("Проверить окно ожидания машины")
    def verify_wait_car_window_displayed(self):
        assert self.check_displayed_element(OrderTaxiLocators.WAIT_CAR_TEXT), \
            "Окно ожидания машины не отображается"

    @allure.step("Проверить окно завершённого заказа")
    def verify_completed_order_window_displayed(self):
        assert self.check_displayed_element(OrderTaxiLocators.ORDER_HEADER_TITLE), \
            "Окно завершённого заказа не отображается"
        assert self.check_displayed_element(OrderTaxiLocators.CAR_NUMBER), \
            "Номер машины не отображается"
        assert self.check_displayed_element(OrderTaxiLocators.DRIVER_NAME), \
            "Имя водителя не отображается"
        assert self.check_displayed_element(OrderTaxiLocators.RATING), \
            "Рейтинг водителя не отображается"

    @allure.step("Нажать кнопку 'Детали' в блоке 'Еще про поездку'")
    def click_details_button(self):
        self.click_element(OrderTaxiLocators.DETAILS_BUTTON)

    @allure.step("Нажать кнопку 'Отменить' и проверить закрытие окна")
    def cancel_order(self):
        self.click_element(OrderTaxiLocators.CANCEL_BUTTON)
        assert not self.check_displayed_element(OrderTaxiLocators.ORDER_HEADER_TITLE), \
            "Окно заказа не закрылось после отмены"


    @allure.step("Проверить, что стоимость в деталях соответствует выбранному тарифу")
    def verify_price_in_details(self, expected_price):
        actual_price_text = self.get_text_from_element(OrderTaxiLocators.DETAILS_PRICE)
        actual_price = int(''.join(filter(str.isdigit, actual_price_text)))
        assert expected_price == actual_price, f"Ожидалась стоимость '{expected_price}', получено '{actual_price}'"

    @allure.step("Получить цену выбранного тарифа '{fare_name}'")
    def get_selected_fare_price(self, fare_name):
        fares = self.get_all_fares_elements()
        for fare in fares:
            title = fare.find_element(*OrderTaxiLocators.FARE_TITLE).text
            if title == fare_name:
                price_text: str = fare.find_element(*OrderTaxiLocators.FARE_WORK_PRICE).text
                # возвращаем только цифры
                return int(''.join(filter(str.isdigit, price_text)))
        raise ValueError(f"Тариф с названием '{fare_name}' не найден")
