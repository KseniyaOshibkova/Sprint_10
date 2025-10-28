import allure



@allure.feature("Отрисовка маршрута на карте")
class TestDrawingRoute:

    @allure.title("Проверка отрисовки маршрута при вводе разных адресов")
    def test_drawing_route_with_different_addresses(self, driver, drawing_route_page):
        drawing_route_page.drawing_route_different_address()
