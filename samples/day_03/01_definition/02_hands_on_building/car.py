class Car:
    distance = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.distance = 0

    def drive(self, dist):
        self.distance += dist
        Car.distance += dist

car_1 = Car("Toyota","Corolla")
car_1.drive(3)

car_2 = Car("Honda","Civic")
car_2.drive(10)

print("Car 1 Distance:", car_1.distance)
print("Car 2 Distance:", car_2.distance)
print("Total Distance:", Car.distance)

