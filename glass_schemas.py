import json
from re import fullmatch, search

import exceptions
from glass_codes import windshield, rear_window, side_window


class Glass:
    def __init__(self, eurocode: str):
        if not self.is_eurocode_correct(eurocode):
            raise exceptions.InvalidEurocodeError
        self.eurocode = eurocode
        self.data = self.get_data(eurocode[4])
        self.car_model, self.car_years = self.get_car_model(eurocode[:4])
        self.glass_type = self.data.type[eurocode[4]]
        self.color = self.data.color[eurocode[5:7]]
        self.characteristics = self.get_characteristics(eurocode[9:])

    @staticmethod
    def is_eurocode_correct(eurocode: str) -> bool:
        pattern = r'[0-9A-Z]{4}[ABCDEFHMLRT][A-Z]{2}[0-9A-Z]{,8}'
        result = fullmatch(pattern, eurocode)
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
    def get_data(code: str):
        if code in 'ACD':
            return windshield
        elif code in 'BE':
            return rear_window
        elif code in 'FHLMRT':
            return side_window

    def get_characteristics(self, code: str):
        result = []
        pattern = r'[A-Z]*?(?=[1-9])'
        string = search(pattern, code).group()
        for char in string:
            if char in self.data.characteristic:
                result.append(self.data.characteristic[char])
        return result
