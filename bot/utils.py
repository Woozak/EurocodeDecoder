import requests
import json


def get_eurocode_data(eurocode: str) -> dict:
    url = f'http://127.0.0.1:8000/decode/{eurocode}'
    data = requests.get(url).json()
    return data


def decode_eurocode(eurocode: str):
    data = get_eurocode_data(eurocode)
    with open('translation.json', 'r', encoding='utf-8') as file:
        translation = json.load(file)

    glass_info = []
    for key, value in data.items():
        if key == 'eurocode':
            continue
        elif key == 'characteristic':
            string = f'{translation[key]}: <b>{', '.join(value).capitalize()}</b>'
        else:
            string = f'{translation[key]}: <b>{value}</b>'
        glass_info.append(string)

    return '\n'.join(glass_info)
