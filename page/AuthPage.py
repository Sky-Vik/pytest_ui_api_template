import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://trello.com/login"
        self.__driver = driver

    @allure.step("Перейти на страницу авторизации")
    def go(self):
        self.__driver.get(self.__url)

    @allure.step("Авторизоваться под {email}:{password}")
    def login_as(self, email: str, password: str):

        # Ожидаем появления поля ввода логина
        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located((By.
                                                 CSS_SELECTOR, "#username"))))

        (self.__driver.find_element(By.CSS_SELECTOR, "#username").
         send_keys(email))
        (self.__driver.find_element(By.CSS_SELECTOR, "#login-submit").
         click())

        # Ожидаем появления поля ввода пароля
        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located((By.
                                                 CSS_SELECTOR, "#password"))))

        (self.__driver.find_element(By.CSS_SELECTOR, "#password").
         send_keys(password))
        (self.__driver.find_element(By.CSS_SELECTOR, "#login-submit").
         click())

        # Ожидаем, когда отрисуется блок с досками
        # (убеждаемся что главная страница полностью загружена)
        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located((
             By.CLASS_NAME, "content-all-boards"))))
        # в конспекте      '[data-loading="False"]'))))
