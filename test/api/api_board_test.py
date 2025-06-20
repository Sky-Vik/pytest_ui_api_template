import allure
from api.BoardApi import BoardApi


def test_create_board(
        api_client: BoardApi, delete_board: dict, test_data: dict):
    org_id = test_data.get("org_id")
    with allure.step("Подсчет количества досок до создания новой доски"):
        board_list_before = api_client.get_all_boards_by_org_id(org_id)

    with allure.step("Создание тестовой доски"):
        resp = api_client.create_board("New board to be deleted")

    with allure.step("Удаление тестовой доски после теста"):
        delete_board["board_id"] = resp.get("id")

    with allure.step("Подсчет количества досок после создания новой доски"):
        board_list_after = api_client.get_all_boards_by_org_id(org_id)

    with allure.step("Проверка: количество досок увеличилось на 1"):
        assert len(board_list_after) - len(board_list_before) == 1


def test_delete_board(
        api_client: BoardApi, dummy_board_id: str, test_data: dict):

    org_id = test_data.get("org_id")
    with allure.step("Подсчет количества досок до удаления доски"):
        board_list_before = api_client.get_all_boards_by_org_id(org_id)

    with allure.step("Удаляем доску"):
        api_client.delete_board_by_id(dummy_board_id)

    with allure.step("Подсчет количества досок до удаления доски"):
        board_list_after = api_client.get_all_boards_by_org_id(org_id)

    with allure.step("Проверка: количество досок уменьшилось на 1"):
        assert len(board_list_before) - len(board_list_after) == 1
