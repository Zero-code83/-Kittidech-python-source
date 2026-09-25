class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.courses = []

    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old."

    def add_course(self, course_name):
        self.courses.append(course_name)
        return f"Enrolled in {course_name}"

    def show_courses(self):
        return f"Courses: {', '.join(self.courses)}"


student1 = Student("Somchai", 20)
student2 = Student("Somsri", 19)

print(student1.introduce())
print(student1.add_course("Python Programming"))
print(student1.add_course("Data Structures"))
print(student1.show_courses())

student1.age = 21

print(student2.introduce())
print(student2.add_course("Math and stat"))
print(student2.show_courses())  # แก้ไขจาก show_course() เป็น show_courses()