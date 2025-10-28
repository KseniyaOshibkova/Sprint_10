import pathlib
import re

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def waiting_for_element(self, locator):
        """Ожидает заданный элемент"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def check_current_url(self, url):
        """Проверяет переход на страницу"""
        WebDriverWait(self.driver, 5).until(EC.url_to_be(url))
        return self.driver.current_url == url


    def find_elements(self, locator):
        """Ищет элемент по локатору"""
        by, value = locator
        return self.driver.find_elements(by, value)


    def get_text_from_element(self, locator):
        return self.find_element(locator).text


    def find_element(self, locator):
        """Ищет элемент по локатору"""
        by, value = locator
        return self.driver.find_element(by, value)


    def click_element(self, locator, timeout=25):
        """Кликает по элементу"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()


    def fill_input(self, locator, value):
        """Заполняет поле ввода"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(value)


    def fill_inputs(self, locators_and_values):
        """Заполняет поля ввода переданные в списке"""
        for locator, value in locators_and_values:
            self.fill_input(locator, value)


    def check_displayed_element(self, locator):
        """Проверяет отображение элемента"""
        element = self.waiting_for_element(locator)
        return element.is_displayed()


    def check_not_displayed_element(self, locator):
        """Проверяет, что элемент не отображается"""
        return self.wait.until(EC.invisibility_of_element_located(locator))


    def is_element_in_container(self, container_locator, element_locator, timeout=10):
        """Проверяет, что элемент с заданным локатором отображается внутри указанного контейнера"""
        with allure.step(f'Проверка, что элемент {element_locator} отображается в контейнере {container_locator}'):
            container = self.driver.find_element(*container_locator)
            element = WebDriverWait(container, timeout).until(
                EC.visibility_of_element_located(element_locator))
            return element.is_displayed()


    def drag_and_drop(self, source_element, target_element):
        """Выполняет перетаскивание элемента source в элемент target"""
        action = ActionChains(self.driver)
        action.drag_and_drop(source_element, target_element).perform()


    def scroll_to_element(self, locator):
        """Скроллит страницу до элемента"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def wait_for_text_change(self, locator, old_text):
        """Ждёт, пока текст элемента сменится с old_text на любой другой и возвращает новый текст"""
        return self.wait.until(lambda d: (text := self.find_element(locator).text.strip()) != old_text and text)

    @staticmethod
    def get_asset_path(filename):
        """Возвращает абсолютный путь к файлу из папки assets"""
        project_root = pathlib.Path(__file__).parent.parent  # поднимаемся на уровень проекта
        assets_dir = project_root / "assets"
        return str(assets_dir / filename)


    def check_current_url_contains(self, expected_part: str) -> bool:
        """Проверяет, что текущий URL содержит указанную подстроку"""
        current_url = self.driver.current_url
        return expected_part in current_url


    def get_current_url(self) -> str:
        """Возвращает текущий URL страницы"""
        return self.driver.current_url


    def wait_for_element_to_be_clickable(self, locator):
        """Ждёт, пока элемент станет кликабельным"""
        return self.wait.until(EC.element_to_be_clickable(locator))


    def move_to_element(self, locator):
        """Наводит таргет на элемент"""
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()


    @staticmethod
    def extract_numbers_with_regex(text):
        """Получение стоимости"""
        return re.findall(r'\d+', text)
