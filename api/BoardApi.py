import requests


class BoardApi:
    def __init__(self, base_url: str, api_key: str, api_token: str) -> None:
        self.base_url = base_url
        self.api_key = api_key
        self.api_token = api_token

    def get_all_boards_by_org_id(self, org_id: str) -> dict:
        parameters = {
            'key': self.api_key,
            'token': self.api_token
            }
        path = ("{trello}/organizations/{id}/boards".format(
            trello=self.base_url, id=org_id))
        # path = ("{trello}/organizations/{id}/boards?key={key}&token={token}"
        # .format(trello=self.base_url, id=org_id, key=self.api_key,
        # token=self.api_token))
        resp = requests.get(path, params=parameters)
        return resp.json()

    def create_board(self, name, default_lists=True):
        body = {
            'defaultLists': default_lists,
            'name': name}
        parameters = {
            'key': self.api_key,
            'token': self.api_token
            }
        path = "{trello}/boards/".format(trello=self.base_url)
        resp = requests.post(path, json=body, params=parameters)

        return resp.json()

    def delete_board_by_id(self, id: str):
        parameters = {
            'key': self.api_key,
            'token': self.api_token
            }
        path = ("{trello}/boards/{board_id}".format(
            trello=self.base_url, board_id=id))
        resp = requests.delete(path, params=parameters)

        return resp.json()
