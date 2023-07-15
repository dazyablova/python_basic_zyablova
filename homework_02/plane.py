from base import Vehicle
from homework_02 import exceptions

"""
создайте класс `Plane`, наследник `Vehicle`
"""


class Plane(Vehicle):
    def __init__(self, brand, model, year, max_cargo):
        super().__init__(brand, model, year)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, amount):
        if self.cargo + amount > self.max_cargo:
            raise exceptions.CargoOverload("Cargo overload")
        self.cargo += amount

    def remove_all_cargo(self):
        current_cargo = self.cargo
        self.cargo = 0
        return current_cargo
