# Define the car class
class car:
    def __init__ (self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    # method to return the description of the car
    def describe(self):
        return f"This is a car {self.make} {self.model} colored {self.color} with a year model of {self.year}."

# Instance of the car class
my_car = car("Toyota", "Land Cruiser", 2025, "White")

# Print the description of the car
print(my_car.describe())