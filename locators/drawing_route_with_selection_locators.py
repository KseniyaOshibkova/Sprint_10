from selenium.webdriver.common.by import By

class DrawingRouteWithSelectionLocators:
    BLOCK_ROUTE = (By.CSS_SELECTOR, ".type-picker.shown .results-container")
    PRICE = (By.CSS_SELECTOR, ".type-picker.shown .results-container .results-text .text")
    DURATION = (By.CSS_SELECTOR, ".type-picker.shown .results-container .results-text .duration")
    OPTIMAL_MODE = By.XPATH, "//div[contains(text(), 'Оптимальный')]"
