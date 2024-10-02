import json
from re import fullmatch, IGNORECASE

import exceptions


class Glass:
    def __init__(self, eurocode: str):
        if not self.is_eurocode_correct(eurocode):
            raise exceptions.InvalidEurocodeError
        self.car_model, self.car_years = self.get_car_model(eurocode[:4])
        self.glass_type = self.get_glass_type(eurocode[4])

    @staticmethod
    def is_eurocode_correct(eurocode: str) -> bool:
        pattern = r'[0-9A-Z]{4}[ABCDEFHMLRT][A-Z]{2}[0-9A-Z]{,8}'
        result = fullmatch(pattern, eurocode, flags=IGNORECASE)
        return bool(result)

    @staticmethod
    def get_car_model(code: str):
        with open('glass_codes/car_models.json', 'r', encoding='utf-8') as file:
            car_models = json.load(file)
            try:
                car_model = car_models[code]
                return car_model.values()
            except KeyError:
                raise exceptions.EurocodeNotFoundError

    @staticmethod
    def get_glass_type(code: str):
        with open('glass_codes/glass_types.json', 'r', encoding='utf-8') as file:
            glass_types = json.load(file)
            for side in glass_types:
                if code in glass_types[side]:
                    return glass_types[side][code]
