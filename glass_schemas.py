import json
import exceptions


class Glass:
    def __init__(self, eurocode: str):
        self.car_model, self.car_years = self.get_car_model(eurocode[:4])
        self.glass_type = self.get_glass_type(eurocode[4])

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
                return glass_types[side][code]
