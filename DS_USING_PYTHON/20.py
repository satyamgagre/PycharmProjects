# Introduction to OOPs concepts

# lets create a class
class Person:
    def __init__(self, name, age):
        #initialize the 'name' attribute of the Person objects
            self.name = name
        # initialize the 'age' attribute of the Person objects
            self.age = age
p1 = Person("Satyqm", 21)
# print the 'name' attribute of the Person object, which is Satyam
print(p1.name)

# print the 'age' attribute of the Person object, which is 21
print(p1.age)

# update the 'age' attribute of the p1 object to 22
p1.age = 22

# Print the updated 'age' attribute of the p1 object , which is 22
print(p1.age)

# Delete the 'age' attribute of the p1 object
del p1.age

# This line will raise an AttributeError
print(p1.age)