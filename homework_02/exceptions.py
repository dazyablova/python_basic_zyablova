"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    def __init__(self):
        super().__init__()


class NotEnoughFuel(Exception):
    def __init__(self):
        super().__init__()


class CargoOverload(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class VehicleNotStartedError(Exception):
    def __init__(self):
        super().__init__()
