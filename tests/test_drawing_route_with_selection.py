import allure


@allure.feature("Отрисовка блока выбора маршрута")
class TestDrawingRouteSelectionBlock:

    @allure.title("Проверка отображения блока выбора маршрута при вводе разных адресов")
    def test_route_selection_block_with_different_addresses(
            self, driver, drawing_route_page, drawing_route_with_selection_page):
        drawing_route_page.input_different_point()
        drawing_route_with_selection_page.drawing_route_block_different_address()

    @allure.title("Проверка отображения блока выбора маршрута при вводе одинаковых адресов")
    def test_route_selection_block_with_equal_addresses(
            self, driver, drawing_route_page, drawing_route_with_selection_page):
        drawing_route_page.input_equal_point()
        drawing_route_with_selection_page.drawing_route_block_equal_address()
