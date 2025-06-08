from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver

    def get_current_url(self) -> str:
        return self.__driver.current_url

    # Нажимаем на иконку с именем в верхнем правом углу:
    def open_menu(self):
        self.__driver.find_element(By.CSS_SELECTOR,
                                   '[data-testid="header-member-menu-avatar"]'
                                   ).click()

    # Получаем информацию о пользователе:
    def get_account_info(self) -> list[str]:
        # Ожидаем полной загрузки меню
        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                 '[data-testid="account-menu-account-section"]'))))
        container = self.__driver.find_element(By.CSS_SELECTOR,
                                               '[data-testid="account-menu-account-section"]>div>div:last-child')
        fields = container.find_elements(By.CSS_SELECTOR, 'div')
        name = fields[0].text
        email = fields[1].text
        # Возвращаем имя и почту пользователя:
        return [name, email]
