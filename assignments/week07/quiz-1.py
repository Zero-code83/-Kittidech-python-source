"""
    สร้าง class Rectangle โดยกำหนดให้
    - มี attribute ชื่อ length และ width ที่เก็บข้อมูลความยาวและความกว้างของสี่เหลี่ยม
    - มี method ชื่อ get_area() ที่คืนค่าพื้นที่ของสี่เหลี่ยม
    - มี method ชื่อ get_perimeter() ที่คืนค่ารอบรูปของสี่เหลี่ยม
"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    
    # Method to get the area
    def get_area(self):
        pass
        return f"Area: {self.length * self.width}"

    # Method to get the perimeter
    def get_perimeter(self):
        pass
        return f"Perimeter: {2 * (self.length + self.width)}"



rect = Rectangle(10, 5)
print(rect.get_area())       # Should print 50
print(rect.get_perimeter())  # Should print 30
print(rect.get_perimeter())  # Should print 30

class Circle:
    # circle ต้องใช้ข้อมูลอะไรบ้าง เพื่อคำนวณ พท.และเส้นรอบรูป
    def __init__(self, radius):
        self.radius = radius

    # Method to get the area สูตรเดิมไหม
    def get_area(self):
        return f"Area: {3.14 * (self.radius ** 2)}"

    # Method to get the perimeter
    def get_perimeter(self):
        return f"Perimeter: {2 * (3.14 * self.radius)}"

myCircle = Circle(7)
print(myCircle.get_area())
print(myCircle.get_perimeter())