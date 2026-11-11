
# Name: Andrew Hoewing
# File: vehicle.py
# Description: This program uses classes to collect and display
# information about a car.

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__("car")
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


# Get information from the user
year = input("Enter the year: ")
make = input("Enter the make: ")
model = input("Enter the model: ")
doors = input("Enter the number of doors (2 or 4): ")
roof = input("Enter the roof type (solid or sun roof): ")

# Create an Automobile object
car = Automobile(year, make, model, doors, roof)

# Display the vehicle information
print("\nVehicle Information:")
print("Vehicle type:", car.vehicle_type)
print("Year:", car.year)
print("Make:", car.make)
print("Model:", car.model)
print("Number of doors:", car.doors)
print("Type of roof:", car.roof)
