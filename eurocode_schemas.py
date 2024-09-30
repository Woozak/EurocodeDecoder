class Glass:
    def __init__(self, eurocode: str):
        self.car_model = self.get_car_model(eurocode[:4])
        self.glass_type = self.get_glass_type(eurocode[4])

    def get_car_model(self, code: str):
        pass

    def get_glass_type(self, code: str):
        pass
