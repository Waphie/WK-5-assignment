# Assignment 1: Design Your Own Class!
# Superhero Class with Inheritance and Encapsulation

class Superhero:
    def __init__(self, name, power, strength_level):
        self.name = name
        self.power = power
        self.__strength_level = strength_level  # Encapsulated attribute

    def show_info(self):
        return f"{self.name} has the power of {self.power}."

    def get_strength(self):
        return self.__strength_level

    def set_strength(self, new_strength):
        if new_strength > 0:
            self.__strength_level = new_strength
        else:
            print("Strength must be positive!")

# Subclass: FlyingSuperhero
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, strength_level, flight_speed):
        super().__init__(name, power, strength_level)
        self.flight_speed = flight_speed

    def fly(self):
        return f"{self.name} is flying at {self.flight_speed} km/h!"

# Example Usage
hero1 = Superhero("ShadowStrike", "Invisibility", 85)
print(hero1.show_info())
print("Strength level:", hero1.get_strength())
hero1.set_strength(95)
print("Updated strength:", hero1.get_strength())

hero2 = FlyingSuperhero("SkyBlaze", "Fire Flight", 100, 300)
print(hero2.show_info())
print(hero2.fly())


# Activity 2: Polymorphism Challenge
class Vehicle:
    def move(self):
        pass  # To be overridden

class Car(Vehicle):
    def move(self):
        print("Driving \U0001F697")

class Plane(Vehicle):
    def move(self):
        print("Flying \u2708\ufe0f")

class Boat(Vehicle):
    def move(self):
        print("Sailing \U0001F6A4")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
