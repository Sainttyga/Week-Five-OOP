class Vehicle: 
    def move(self):
        print("This vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Driving on the road")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky")

class Boat(Vehicle):
    def move(self):
        print("Sailing across the water")

# Function to demonstrate polymorphism
def travel(vehicle):
    vehicle.move()

# Create objects
my_car = Car()
my_plane = Plane()
my_boat = Boat()

# Use the travel function to see polymorphism in action
travel(my_car)
travel(my_plane)
travel(my_boat)