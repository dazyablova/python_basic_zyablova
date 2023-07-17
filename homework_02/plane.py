from homework_02 import exceptions
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload

"""
создайте класс `Plane`, наследник `Vehicle`
"""


class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo=10):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, amount):
        if self.cargo + amount > self.max_cargo:
            raise CargoOverload("Cargo overload!")
        else:
            self.cargo += amount

    def remove_all_cargo(self):
        prev_cargo = self.cargo
        self.cargo = 0
        return prev_cargo

