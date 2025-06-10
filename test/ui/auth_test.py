import allure
from pages.AuthPage import AuthPage
from pages.MainPage import MainPage


def test_auth(browser, test_data: dict):
    email = test_data.get("email")
    password = test_data.get("pass")
    username = test_data.get("username")
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    main_page.open_menu()

    info = main_page.get_account_info()
    current_url = main_page.get_current_url()

    with allure.step(
        f"Проверить, что URL {current_url} заканчивается на _k202506/boards"
    ):
        assert current_url.endswith("_k202506/boards")

    with allure.step("Проверить, что указаны данные пользователя"):
        with allure.step("Имя пользователя должно быть " + username):
            assert info[0] == username
        with allure.step("Почта пользователя должна быть " + email):
            assert info[1] == email
