class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.spaces = {"big": big, "medium": medium, "small": small}
        self.car_sizes = {1: "big", 2: "medium", 3: "small"}

    def addCar(self, carType: int) -> bool:
        car_size = self.car_sizes[carType]
        if self.spaces[car_size] > 0:
            self.spaces[car_size] -= 1
            return True
        else:
            return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)