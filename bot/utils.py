import requests
import json


def get_eurocode_data(eurocode: str) -> dict:
    url = f'http://127.0.0.1:8000/decode/{eurocode}'
    response = requests.get(url)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError:
        if response.status_code == 400:
            raise ValueError('Некорректный еврокод')
        elif response.status_code == 404:
            raise ValueError('Еврокод не найден')
        else:
            raise ValueError('Произошла ошибка, попробуйте снова')


def decode_eurocode(eurocode: str) -> str:
    try:
        data = get_eurocode_data(eurocode)
        with open('translation.json', 'r', encoding='utf-8') as file:
            translation = json.load(file)
        glass_info = []
        for key, value in data.items():
            if key == 'eurocode':
                continue
            elif key == 'characteristic':
                string = f'{translation[key]}: <b>{', '.join(value)}</b>'
            else:
                string = f'{translation[key]}: <b>{value}</b>'
            glass_info.append(string)
        return '\n'.join(glass_info)
    except ValueError as error:
        return str(error)
