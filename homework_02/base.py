from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel, VehicleNotStartedError


class Vehicle(ABC):
    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 0
    def __init__(self, weight: int, fuel: int, fuel_consumption: int) -> None :
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started is False:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError


    def move(self, distance):
        fuel_need = distance * self.fuel_consumption
        if fuel_need > self.fuel:
            raise NotEnoughFuel
        else:
            self.fuel -= fuel_need