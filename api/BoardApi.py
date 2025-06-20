import requests
import allure


class BoardApi:
    @allure.step("API. URL:{base_url}, api_key:{api_key}, token:{api_token}.")
    def __init__(self, base_url: str, api_key: str, api_token: str) -> None:
        self.base_url = base_url
        self.params = {
            'key': api_key,
            'token': api_token
            }

    @allure.step("Запросить список всех досок для организации {org_id}")
    def get_all_boards_by_org_id(self, org_id: str) -> dict:

        path = ("{trello}/organizations/{id}/boards".format(
            trello=self.base_url, id=org_id))

        # path = ("{trello}/organizations/{id}/boards?key={key}&token={token}"
        # .format(trello=self.base_url, id=org_id, key=self.api_key,
        # token=self.api_token))
        resp = requests.get(path, params=self.params)
        return resp.json()

    @allure.step("Создать доску {name}")
    def create_board(self, name, default_lists=True):
        body = {
            'defaultLists': default_lists,
            'name': name}

        path = "{trello}/boards/".format(trello=self.base_url)
        resp = requests.post(path, json=body, params=self.params)

        return resp.json()

    @allure.step("Удалить доску {id}")
    def delete_board_by_id(self, id: str):

        path = ("{trello}/boards/{board_id}".format(
            trello=self.base_url, board_id=id))
        resp = requests.delete(path, params=self.params)

        return resp.json()
