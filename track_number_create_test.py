# Санеева Ольга, 17ая когорта - Финальный проект. Инженер по тестированию плюс
import sending_requests


def get_track_number_of_order():
    track_number = sending_requests.post_new_order()
    return track_number.json()["track"]


def positive_assert():
    track_number = get_track_number_of_order()
    get_response = sending_requests.get_order_info(track_number)
    assert get_response.status_code == 200

def test_order():
    positive_assert()