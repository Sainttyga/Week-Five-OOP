# Base class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        print(f"I am {self.name}, and I protect {self.city} with my {self.power}!")

    def use_power(self):
        print(f"{self.name} uses their {self.power}!")

# Subclass with encapsulation and method overriding
class Speedster(Superhero):
    def __init__(self, name, city, max_speed):
        super().__init__(name, "Super Speed", city)
        self.__max_speed = max_speed  # Encapsulated (private) attribute

    def reveal_speed(self):
        print(f"{self.name}'s top speed is {self.__max_speed} km/h!")

    # Overriding use_power() to show different behavior
    def use_power(self):
        print(f"{self.name} zooms through {self.city} at lightning speed!")

# Create superhero objects
hero1 = Superhero("Spider-Man", "Superman", "Betman")
hero2 = Speedster("Black Panther", "Captain America", 3000)

# Call methods
hero1.introduce()
hero1.use_power()

print()  # Just for spacing

hero2.introduce()
hero2.use_power()
hero2.reveal_speed()
