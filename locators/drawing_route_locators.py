from selenium.webdriver.common.by import By

class DrawingRouteLocators:
    FROM_INPUT = (By.XPATH, "//input[@id='from']")
    TO_INPUT = (By.XPATH, "//input[@id='to']")

    ROUTE_POINT_A = By.XPATH, "//ymaps[text()='улица Хамовнический Вал, 34']" # точка откуда
    ROUTE_POINT_B = By.XPATH, "//ymaps[text()='Зубовский бульвар, 37']" # точка куда
