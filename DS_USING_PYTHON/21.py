# Concept of Inheritance
# * Code Reusability
# * Hierarchy and Organization
# * Overriding and Extension

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, "is", self.age)


# Creating object of Person
p1 = Person("Satyam", 21)
p1.display()   # Output: Satyam is 21


# Child class inheriting Person
class Student(Person):
    def __init__(self, name, age, roll_no=None):
        # call the parent class's constructor
        super().__init__(name, age)
        self.roll_no = roll_no   # extension (extra attribute for Student)

    # overriding display method
    def display(self):
        if self.roll_no:
            print(f"{self.name} is {self.age} years old, Roll No: {self.roll_no}")
        else:
            super().display()   # call parent display if no roll_no


# Creating object of Student
p2 = Student("Satya", 21, roll_no=101)
p2.display()   # Output: Satya is 21 years old, Roll No: 101
