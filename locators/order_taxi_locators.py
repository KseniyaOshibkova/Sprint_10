from selenium.webdriver.common.by import By

class OrderTaxiLocators:
    # Кнопки заказа
    ORDER_TAXI_BUTTON = (By.XPATH, "//button[text()='Вызвать такси']")
    CANCEL_BUTTON = (By.XPATH, "//div[contains(text(), 'Отменить')]/preceding-sibling::button")
    DETAILS_BUTTON = (By.XPATH, "//div[contains(text(), 'Детали')]/preceding-sibling::button")
    SMART_BUTTON = (By.XPATH, "//button[@type='button' and contains(@class, 'smart-button')]")

    # Текстовые элементы окна заказа
    WAIT_CAR_TEXT = (By.XPATH, "//div[contains(text(), 'Поиск машины')]")
    ORDER_HEADER_TITLE = (By.CLASS_NAME, "order-header-title")
    DETAILS_PRICE = (By.XPATH, "//div[contains(text(), 'Стоимость - ')]")

    # Информация о машине и водителе
    CAR_NUMBER = (By.CLASS_NAME, "number")
    DRIVER_NAME = (By.XPATH, "//div[contains(@style, 'cursor')]")
    RATING = (By.CLASS_NAME, "order-btn-rating")

    # Тарифы
    FARE_CARDS = (By.CLASS_NAME, "tcard")
    FARE_TITLE = (By.CLASS_NAME, "tcard-title")
    FARE_INFO_BUTTON = (By.CLASS_NAME, "i-dPrefix")
    TESTING_HOVER_FARE_DESCRIPTION = (By.XPATH, "//div[contains(@class, 'show border')]/div[@class='i-floating']/div"
                                                "[@class='i-dPrefix']")
    FARE_WORK = (By.XPATH, "//div[contains(text(), 'Рабочий')]/..")
    FARE_WORK_PRICE = (By.XPATH, "//div[contains(text(), 'Рабочий')]/following-sibling::div")
    ACTIVE_ROUTE_TYPE = (By.XPATH, "//div[contains(@class, 'type') and contains(@class, 'active')]")

    # Поля формы заказа
    PHONE_FIELD = (By.CLASS_NAME, "np-text")
    PAYMENT_FIELD = (By.CLASS_NAME, "pp-text")
    COMMENT_FIELD = (By.ID, "comment")
    REQUIREMENTS_FIELD = (By.CLASS_NAME, "reqs-head")
    CHECKBOX_TABLE_FOR_NOTEBOOK = (By.XPATH, "//span[contains(@class, 'slider round')]")

    # Тип маршрута
    ROUTE_TYPE_FAST = (By.XPATH, "//div[text()='Быстрый']")
