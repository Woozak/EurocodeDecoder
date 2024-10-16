import json
from re import fullmatch, search
from pydantic import BaseModel

from app import exceptions
from app.glass_codes import windshield, rear_window, side_window


class Glass:
    def __init__(self, eurocode: str):
        self.eurocode = eurocode
        self.data = self.get_data(eurocode[4])
        self.is_eurocode_correct(self.data.pattern, eurocode)

        self.car_model, self.car_years = self.get_car_model(eurocode[:4])
        self.glass_type = self.data.type[eurocode[4]]
        self.color = self.get_attribute(self.data.color, eurocode[5:7])
        self.modification = self.get_modification(self.data.modification, eurocode[-2:])

    @staticmethod
    def get_data(code: str):
        if code in 'ACD':
            return windshield
        elif code in 'BE':
            return rear_window
        elif code in 'FHLMRT':
            return side_window

    @staticmethod
    def is_eurocode_correct(pattern: str, eurocode: str) -> None:
        result = fullmatch(pattern, eurocode)
        if not result:
            raise exceptions.InvalidEurocodeError

    @staticmethod
    def get_car_model(code: str) -> tuple[str, str]:
        with open('glass_codes/car_models.json', 'r', encoding='utf-8') as file:
            car_models = json.load(file)
            try:
                car_model = car_models[code]
                return car_model.values()
            except KeyError:
                raise exceptions.EurocodeNotFoundError

    @staticmethod
    def get_attribute(data, code: str) -> str:
        try:
            return data[code]
        except KeyError:
            raise exceptions.InvalidEurocodeError

    @staticmethod
    def get_characteristic(data, code: str) -> list[str]:
        characteristic = []
        pattern = r'[^1-9]*'
        string = search(pattern, code).group()
        if len(string) != len(set(string)):
            raise exceptions.InvalidEurocodeError
        for char in string:
            try:
                characteristic.append(data[char])
            except KeyError:
                raise exceptions.InvalidEurocodeError
        return characteristic

    @staticmethod
    def get_modification(data, code: str) -> str | None:
        for mod in data:
            if code in mod:
                return data[mod]


class Windshield(Glass):
    def __init__(self, eurocode: str):
        super().__init__(eurocode)
        self.strip_color = self.data.strip_color[eurocode[7:9]] if eurocode[7:9] in self.data.strip_color else None
        self.characteristic = self.get_characteristic(
            self.data.characteristic,
            eurocode[9:] if self.strip_color else eurocode[7:]
        )


class RearWindow(Glass):
    def __init__(self, eurocode: str):
        super().__init__(eurocode)
        self.body_type = self.data.body_type[eurocode[7]]
        self.characteristic = self.get_characteristic(self.data.characteristic, eurocode[8:])


class SideWindow(Glass):
    def __init__(self, eurocode: str):
        super().__init__(eurocode)
        self.body_type = self.get_attribute(self.data.body_type, eurocode[7:9])
        self.position = self.get_attribute(self.data.position, eurocode[9:11])
        self.characteristic = self.get_characteristic(self.data.characteristic, eurocode[11:])


class ResponseGlass(BaseModel):
    eurocode: str
    car_model: str
    car_years: str
    glass_type: str
    color: str
    strip_color: str | None = None
    body_type: str | None = None
    position: str | None = None
    characteristic: list[str] = []
    modification: str | None = None
