"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""
class Rectangle:
    def __init__(self, lenght, width):
        self.__length = lenght
        self.__width = width

    def getArea(self):
        print(f"Area of {self.__length} lenth and {self.__width} width = {self.__length * self.__width}")

    def getPerimemter(self):
        print(f"Perimeter of {self.__length} lenth and {self.__width} width = {2 * (self.__length + self.__width)}")

    def isSquare(self):
        print(self.__length == self.__width)

myRectangle = Rectangle(10,5)
myRectangle.____length = 1000
myRectangle.getArea()
myRectangle.getPerimemter()
myRectangle.isSquare()   