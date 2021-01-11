__doc__ = """
Viết script dùng API tạo 1 Trello board với 2 list "Thứ 3", "Thứ 5",
và tạo 12 card ứng với 12 buổi học của lớp, có set due date ứng với các ngày
học.
"""


import requests
import datetime


print("Fill in your API keys")
key = str(input())
print("Fill in your API token")
token = str(input())


def create_boards(board_name):
    url = "https://api.trello.com/1/boards/"
    query = {
        "key": key,
        "token": token,
        "name": board_name,
        "prefs_background": "green",
    }
    response = requests.request("POST", url, params=query)
    board_id = response.json()["id"]
    return board_id


def create_lists(board_id, list_name):
    url = f"https://api.trello.com/1/list"
    query = {"key": key, "token": token, "name": list_name, "idBoard": board_id}
    response = requests.request("POST", url, params=query)
    list_id = response.json()["id"]
    return list_id


def create_cards(list_id, card_name, due_date):
    url = f"https://api.trello.com/1/cards"
    query = {
        "key": key,
        "token": token,
        "name": card_name,
        "idList": list_id,
        "due": due_date,
    }
    response = requests.request("POST", url, params=query)
    card_id = response.json()["id"]
    return card_id


def main():
    board_name = "Pymi 2011HN Timetable"
    board_id = create_boards(board_name)
    list_names = ["Tuesday", "Thursday"]

    for list_name in list_names:
        if list_name == "Tuesday":
            list_id = create_lists(board_id, list_name)
            due_date = datetime.datetime(2020, 11, 26)
            for card_name in [
                "Lesson {}".format(i) for i in range(1, 13) if i % 2 != 0
            ]:
                print(create_cards(list_id, card_name, due_date))
                due_date += datetime.timedelta(days=7)
        else:
            list_id = create_lists(board_id, list_name)
            due_date = datetime.datetime(2020, 11, 28)
            for card_name in [
                "Lesson {}".format(i) for i in range(1, 13) if i % 2 == 0
            ]:
                print(create_cards(list_id, card_name, due_date))
                due_date += datetime.timedelta(days=7)
    print("Your timetable is created successfully")


if __name__ == "__main__":
    main()
