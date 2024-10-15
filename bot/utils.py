import requests


def get_eurocode_data(eurocode: str) -> dict:
    url = f'http://127.0.0.1:8000/decode/{eurocode}'
    data = requests.get(url).json()
    return data


def decode_eurocode(eurocode: str):
    data = get_eurocode_data(eurocode)
    glass_info = (f'Модель авто: <b>{data['car_model']}</b>\n'
                  f'Год выпуска: <b>{data['car_years']}</b>\n'
                  f'Цвет стекла: <b>{data['color']}</b>\n')

    return glass_info
