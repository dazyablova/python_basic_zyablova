from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel, VehicleNotStartedError


class Vehicle(ABC):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance):
        if self.started:
            fuel_needed = distance * self.fuel_consumption
            if self.fuel >= fuel_needed:
                self.fuel -= fuel_needed
            else:
                raise NotEnoughFuel
        else:
            raise VehicleNotStartedError
