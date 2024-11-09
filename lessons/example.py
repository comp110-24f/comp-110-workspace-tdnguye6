"""Python Playground"""


class Car:
    make: str
    model: str
    year: int
    color: str
    mileage: float

    def __init__(self, make: str, model: str, year: int, color: str, mileage: float):
        self.make = make
        self.model = model
        self.year = int
        self.color = str
        self.mileage = float

    def update_mileage(self, miles: float) -> None:
        self.mileage += miles

    def display_info(self) -> None:
        print(f"MAKE: {self.make}")
        print(f"MODEL: {self.model}")
        print(f"YEAR: {self.year}")
        print(f"COLOR: {self.color}")
        print(f"MILEAGE: {self.mileage}")


def calculate_depreciation(my_car: Car, depreciation_rate: float) -> float:
    depreciation: float = my_car.mileage * depreciation_rate
    return depreciation
