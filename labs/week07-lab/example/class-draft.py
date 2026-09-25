"""
programming => การเขียนโปรแกรม
2 types
1) structured programming ==> การเขียนโปรแกรมเชิงโครงสร้าง ==> C, JS, PHP, Python
2) Object-Oriented Programming ==> การเขียนโปรแกรมเชิงวัตถุ ==> Java, C#, Python
"""


# แม่แบบ (Template)
class ClassName:
    """Class docstring"""

    def __init__(self, param1, param2="default"):
        self.attribute = param1
        self.attribute2 = param2

    def method_name(self):
        return f"Result: {self.attribute}"

    def method_name2(self):  # ต้องใส่ self ด้วยเสมอ
        pass


# การนำไปใช้งานจริง
myObj = ClassName("TestValue")
print(myObj.attribute)
resultFromMethod = myObj.method_name()
print(resultFromMethod)
myObj.method_name2()