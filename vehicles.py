# vehicles.py

class Vehicle:
    def move(self):
        print("Moving...")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")



#sample usage

vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
