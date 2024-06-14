# Санеева Ольга, 17ая когорта - Финальный проект. Инженер по тестированию плюс
import requests
import configuration
import data

def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
           json=data.order_body)

def get_order_info(track_number):
    get_order_url = f"{configuration.URL_SERVICE} + {configuration.GET_ORDER_INFO} + '?t=' + {track_number}"
    response = requests.get(get_order_url)
    return response