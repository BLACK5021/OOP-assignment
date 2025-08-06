# superhero.py

class Superhero:
    def __init__(self, name, power, level):
        self.name = name
        self.power = power
        self.__level = level  # encapsulated/private attribute

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Power: {self.power}")
        print(f"Level: {self.__level}")

    def increase_level(self):
        self.__level += 1
        print(f"{self.name}'s level increased to {self.__level}!")

# Subclass demonstrating inheritance
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, level, flight_speed):
        super().__init__(name, power, level)
        self.flight_speed = flight_speed

    def fly(self):
        print(f"{self.name} is flying at {self.flight_speed} km/h!")








#sample usage

hero1 = Superhero("Shadow Ninja", "Invisibility", 5)
hero1.display_info()
hero1.increase_level()

print("-----")

hero2 = FlyingSuperhero("Sky Blaze", "Fire Control", 10, 300)
hero2.display_info()
hero2.fly()
