"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class LowFuelError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class NotEnoughFuel(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class CargoOverload(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class VehicleNotStartedError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)