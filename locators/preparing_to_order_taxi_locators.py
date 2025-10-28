from selenium.webdriver.common.by import By

class PreparingToOrderTaxiLocators:
    MODE_ACTIVE = By.XPATH, "//div[contains(@class, 'mode active')]"
    OPTIMAL_MODE = By.XPATH, "//div[contains(text(), 'Оптимальный')]"
    FAST_MODE = By.XPATH, "//div[contains(text(), 'Быстрый')]"
    SVOY_MODE = By.XPATH, "//div[contains(text(), 'Свой')]"
    TYPES_ACTIVE = By.XPATH, "//div[contains(@class, 'types-container')]/div[contains(@class, 'type')]"
    ORDER_TAXI_BUTTON = (By.XPATH, "//button[text()='Вызвать такси']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Забронировать']")
    SVOY_MODE_TYPE_DRIVE = By.XPATH, "//div[contains(@class, 'drive')]"
    # Блок с результатами маршрута
    RESULTS_CONTAINER = (By.CSS_SELECTOR, ".type-picker.shown .results-container")
    # Стоимость маршрута внутри блока результатов
    PRICE = (By.CSS_SELECTOR, ".type-picker.shown .results-container .results-text .text")
    # Длительность маршрута внутри блока результатов
    DURATION = (By.CSS_SELECTOR, ".type-picker.shown .results-container .results-text .duration")
