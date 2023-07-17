from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel, VehicleNotStartedError


class Vehicle(ABC):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.is_started = False

    def start(self):
        if not self.is_started:
            if self.fuel > 0:
                self.is_started = True
            else:
                raise LowFuelError("Low fuel")

    def move(self, distance):
        fuel_need = distance * self.fuel_consumption
        if fuel_need > self.fuel:
            raise NotEnoughFuel
        else:
            self.fuel -= fuel_need