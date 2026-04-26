# Base Class
class Person:
    def __init__(self, name, age):
        self.name = name          # Encapsulation
        self.age = age

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Inheritance
class Student(Person):
    def __init__(self, name, age, roll, marks):
        super().__init__(name, age)
        self.roll = roll
        self.marks = marks

    # Method Overriding (Polymorphism)
    def show(self):
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Roll No: {self.roll}")
        print(f"Marks: {self.marks}")


# Another Child Class
class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def show(self):
        print(f"Teacher Name: {self.name}")
        print(f"Subject: {self.subject}")
        print(f"Salary: {self.salary}")


# Polymorphism Function
def display_info(obj):
    obj.show()


# Abstraction Example
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Main Execution
if __name__ == "__main__":

    # Object Creation
    s1 = Student("Rahul", 20, 101, 85)
    t1 = Teacher("Sharma", 40, "Math", 50000)

    # Polymorphism Call
    display_info(s1)
    print()
    display_info(t1)

    print("\n--- Shape Area ---")
    r = Rectangle(10, 5)
    print("Rectangle Area:", r.area())