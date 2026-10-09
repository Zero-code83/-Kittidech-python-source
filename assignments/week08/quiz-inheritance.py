""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""
class Vehicle:

    def __init__(self , brand, model, year):
        self.brand = brand 
        self.model = model
        self.year = year

    def get_info(self):
        print("Brand: ",self.brand )
        print("Model: ",self.model )
        print("Year: ",self.year )

class Car(Vehicle):

    def __init__(self , brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors

    def get_info(self):
        print("Brand: ",self.brand )
        print("Model: ",self.model )
        print("Year: ",self.year )
        print("Number of Doors: ",self.number_of_doors)

car = Car("Isuzu","D-MAX",2026,4)
car.get_info()