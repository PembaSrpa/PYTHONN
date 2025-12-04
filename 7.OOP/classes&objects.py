
# Example 1: A simple 'Car' class and creating objects (instances) of it
class Car:
    def __init__(self, make, model, year):
        self.make = make    # Instance variable for car make
        self.model = model  # Instance variable for car model
        self.year = year    # Instance variable for car year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

# Creating objects of the Car class
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Accord", 2021)

car1.display_info()  # Output: 2022 Toyota Camry
car2.display_info()  # Output: 2021 Honda Accord


