import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from api.BoardApi import BoardApi
from configuration.ConfigProvider import ConfigProvider


@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):
        timeout = ConfigProvider().getint("ui", "timeout")

        browser_name = ConfigProvider().get("ui", "browser_name")
        if browser_name == "chrome":
            browser = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()))
        else:
            browser = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()))

        browser.implicitly_wait(timeout)
        browser.maximize_window()
        yield browser

    with allure.step("Закрыть браузер"):
        browser.quit()


@pytest.fixture
@allure.step("Создание настроек для авторизации")
def api_client() -> BoardApi:
    url = ConfigProvider().get("api", "base_url")
    resp = (BoardApi(url, "29166818aaf45cfc8665579af6243c22",
                     "ATTA7e7f4a1f0ea51a8c8192aa99feca7209235e829758c09575aed\
bf2b5a6f883f0E6958C82"))
    return resp


@pytest.fixture
@allure.step("Создание сущности класса 'BoardApi' без авторизации")
def api_client_no_auth() -> BoardApi:
    return BoardApi(ConfigProvider().get("api", "base_url"), "")


@pytest.fixture
def dummy_board_id() -> str:
    api = (BoardApi(ConfigProvider().get("api", "base_url"),
                    "29166818aaf45cfc8665579af6243c22",
                    "ATTA7e7f4a1f0ea51a8c8192aa99feca7209235e829758c09575aed\
bf2b5a6f883f0E6958C82"))

    resp = api.create_board("Board to be deleted").get("id")
    return resp


@pytest.fixture
def delete_board():
    dictionary = {"board_id": ""}
    yield dictionary

    api = (BoardApi(ConfigProvider().get("api", "base_url"),
                    "29166818aaf45cfc8665579af6243c22",
                    "ATTA7e7f4a1f0ea51a8c8192aa99feca7209235e829758c09575aed\
bf2b5a6f883f0E6958C82"))
    api.delete_board_by_id(dictionary.get("board_id"))
