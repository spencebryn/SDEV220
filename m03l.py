# Name: Spencer Strange
# File name: m03l.py
# Course: SDEV 220
# Variables/Classes:
#   Vehicle: Super Class; contains attribute for vehicle type
#   Automobile: Class; subclass of Vehicle, adds year, make, model, doors, and roof attributes

# SuperClass: Vehicle
class Vehicle:
	def __init__(self, type):   
		self.type = type 

# SubClass: Automobile from Vehicle
class Automobile(Vehicle):
	def __init__(self, type, year, make, model, doors, roof):
		super().__init__(type) 
		self.year = year
		self.make = make
		self.model = model
		self.doors = doors
		self.roof = roof

# App for inputs
input_vehicletype = input("Type of vehicle: ")
input_year = input("Enter the year: ")
input_make = input("Enter the make: ")
input_model = input("Enter the model: ")
input_doors = input("Enter the number of doors (2 or 4): ")
input_roof = input("Enter if the roof is solid or sun roof: ")
auto = Automobile(input_vehicletype, input_year, input_make, input_model, input_doors, input_roof) 

# Print details
print("Vehicle Type: " + auto.type)
print("Year: " + auto.year)
print("Make: " + auto.make)
print("Model: " + auto.model)
print("No of doors: " + auto.doors)
print("Type of roof: " + auto.roof)