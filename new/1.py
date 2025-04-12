class Vehicle:
    def __init__(self, make, model, year, color):
        self.make = make
        self.year = year
        self.model = model
        self.color = color
    def display_info(self):
        print("Make:", self.make)
        print("Self:", self.year)
        print("Model:", self.model)
        print("Color:", self.color)
    def start(self):
        print("Start Vehicle")
    def stop(self):
        print("Stop Vehicle")
class Car(Vehicle):
    def __init__(self, make, model, year, color, num_doors):
        Vehicle.__init__(self, make, model, year, color)
        self.num_doors = num_doors
    def start(self):
        print("Starting the car")
    def stop(self):
        print("Stopping the car")
class Truck(Vehicle):
    def __init__(self, make, model, year, color, cargo_capacity):
        Vehicle.__init__(self, make, model, year, color)
        self.cargo_capacity = cargo_capacity
    def start(self):
        print("Starting the truck")
    def stop(self):
        print("Stopping the truck")
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, color, has_sidecar):
        Vehicle.__init__(self, make, model, year, color)
    def start(self):
        print("Starting the motorcycle")
    def stop(self):
        print("Stopping the motorcycle")

class Bus(Vehicle):
    def __init__(self, make, model, year, color, num_of_windows):
        Vehicle.__init__(self, make, model, year, color)
    def start(self):
        print("Starting the bus")


class Student:
    def __init__(self,name):
        self.name = name
        print (f"Student{self.name} created")

    def __del__(self):
        print(f"Student {self.name} deleted")
s1 = ("XYZ")
del s1


car = Car("Ford","BMW","2021", "Black",4)
truck = Truck("Ford","BMW","2021","Black",3.5)
motorcycle = Motorcycle("Ford","BMW","2021","Black", True)

object = Myclass()
def start(make, model):
    pass

def start(make, model, color):
    pass
a = 123
print("car info:")
car.display_info()
car.start()
car.stop()

print("\nTruck Info:")
truck.display_info()
truck.start()
truck.stop()

print("\nMotorcycle Info:")
motorcycle.display_info()
motorcycle.start()
motorcycle.stop()



