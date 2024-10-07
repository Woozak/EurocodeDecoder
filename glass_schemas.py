import json
from re import fullmatch, search

import exceptions
from glass_codes import windshield, rear_window, side_window


class Glass:
    def __init__(self, eurocode: str):
        self.is_eurocode_correct(eurocode)

        self.eurocode = eurocode
        self.data = self.get_data(eurocode[4])
        self.car_model, self.car_years = self.get_car_model(eurocode[:4])
        self.glass_type = self.data.type[eurocode[4]]
        self.color = self.data.color[eurocode[5:7]]
        self.modifications = self.get_modifications(eurocode[-2:])

    @staticmethod
    def is_eurocode_correct(eurocode: str):
        pattern = r'[0-9A-Z]{4}[ABCDEFHMLRT][A-Z]{2}[1-9A-Z]{,8}'
        result = fullmatch(pattern, eurocode)
        if not result:
            raise exceptions.InvalidEurocodeError

    @staticmethod
    def get_data(code: str):
        if code in 'ACD':
            return windshield
        elif code in 'BE':
            return rear_window
        elif code in 'FHLMRT':
            return side_window

    @staticmethod
    def get_car_model(code: str):
        with open('glass_codes/car_models.json', 'r', encoding='utf-8') as file:
            car_models = json.load(file)
            try:
                car_model = car_models[code]
                return car_model.values()
            except KeyError:
                raise exceptions.EurocodeNotFoundError

    def get_characteristics(self, code: str):
        characteristics = []
        pattern = r'[^1-9]*'
        string = search(pattern, code).group()
        for char in string:
            characteristics.append(self.data.characteristic[char])
        return characteristics

    def get_modifications(self, code: str):
        for mod in self.data.modification:
            return self.data.modification[mod] if code in mod else None


class Windshield(Glass):
    def __init__(self, eurocode: str):
        super().__init__(eurocode)
        self.strip_color = self.data.strip_color[eurocode[7:9]] if eurocode[7:9] in self.data.strip_color else None
        self.characteristics = self.get_characteristics(eurocode[9:] if self.strip_color else eurocode[7:])


class RearWindow(Glass):
    def __init__(self, eurocode: str):
        super().__init__(eurocode)
        self.body_type = self.data.body_type[eurocode[7]]


class SideWindow(Glass):
    def __init__(self, eurocode: str):
        super().__init__(eurocode)
        self.body_type = self.data.body_type[eurocode[7:9]]
        self.position = self.data.position[eurocode[9:11]]
        self.characteristics = self.get_characteristics(eurocode[11:])
