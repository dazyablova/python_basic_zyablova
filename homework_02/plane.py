from homework_02 import exceptions
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload

"""
создайте класс `Plane`, наследник `Vehicle`
"""


class Plane(Vehicle):
    def __init__(self, brand, model, year, max_cargo):
        super().__init__(weight=0, fuel=0, fuel_consumption=0)
        self.brand = brand
        self.model = model
        self.year = year
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, amount):
        if self.cargo + amount > self.max_cargo:
            raise CargoOverload("Cargo overload")
        self.cargo += amount

    def remove_all_cargo(self):
        current_cargo = self.cargo
        self.cargo = 0
        return current_cargo

class CargoOverload(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message



