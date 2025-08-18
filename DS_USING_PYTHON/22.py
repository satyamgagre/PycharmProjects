# Introduction to Encapsulation
class Person:
    def __init__(self, name, age):
        self.name = name       # public attribute
        self._age = age        # protected attribute (by convention, _ means "internal use")

    def display(self):
        print(self.name, "is", self._age, "years old")

# create object
p1 = Person("Satya", 21)
p1.display()   # Output: Satya is 21 years old

# modifying attribute directly (not good practice, but possible)
p1._age = 22
p1.display()   # Output: Satya is 22 years old

print("_"*100)

class Person:
    def __init__(self, name, _age):
        self.name = name
        self._age = _age
    def display(self):
        print(self.name, "is", self._age, "years old")
    def modify_age(self, new_age):
        self._age = new_age

p1 = Person("Satya", 21)
p1.display()
p1.modify_age(22)
p1.display()
