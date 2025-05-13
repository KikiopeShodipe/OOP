# Define the class Vehicle
class Vehicle:
    def __init__(self, maxspeed, mileage):
        self.max_speed = maxspeed
        self.mileage = mileage
# Ask the user for input
max_speed_input = int(input("Enter the vehicle's maximum speed (in km/h): "))
mileage_input = int(input("Enter the vehicle's mileage (in km): "))
# Create an object of class Vehicle using user input
car = Vehicle(max_speed_input, mileage_input)
# Print the values using the object
print("\nVehicle Information")
print("Maximum Speed:", car.max_speed, "km/h")
print("Mileage:", car.mileage, "km")