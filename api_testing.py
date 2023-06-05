import requests

APIKEY = "c9457264aefb36af5d177a5f6615d33d"
TOKEN = "c217704ffd9ca219e555b0e297a40102806272317f38e4b80a6fa85667cebf30"

URL = "https://api.trello.com/"


# URL = "https://trello.com/u/franik_kaskad/boards"


def get_user_boards():
    endpoints = "1/members/me/boards"
    params = {
        'key': APIKEY,
        'token': TOKEN

    }

    response = requests.get(url=URL + endpoints, json=params)
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()

    print(response_json)


def create_new_board(name):
    endpoint = "1/boards/"
    params = {
        'key': APIKEY,
        'token': TOKEN,
        'name': name
    }

    response = requests.post(url=URL + endpoint, json=params)
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)


if __name__ == "__main__":
    # get_user_boards()
    create_new_board("Test Automation")
