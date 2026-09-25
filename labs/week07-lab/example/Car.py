class Car:
    # Class attribute (shared by all instances)
    wheels = 4
    vehicle_type = "Car"

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0

    def drive(self, distance):
        self.mileage += distance
        return f"Drove {distance} km. Total mileage: {self.mileage} km"

    def get_info(self):
        return (
            f"{self.year} {self.brand} {self.model} - Mileage: {self.mileage} km"
        )

    @classmethod
    def get_vehicle_type(cls):
        return cls.vehicle_type


# Creating instances
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2021)
car3 = Car("Isuzu", "D-Max", 2022)

# Accessing class attributes
print(f"All cars have {Car.wheels} wheels")
print(Car.get_vehicle_type())

# Accessing instance methods
print(car1.get_info())
print(car2.get_info())

# Using methods
print(car1.drive(100))  # car1 mileage = 100
print(car2.drive(250))  # car2 mileage = 250
print(car1.drive(200))  # car1 mileage = 300