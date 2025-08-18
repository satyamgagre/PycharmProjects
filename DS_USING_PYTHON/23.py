# ------------------------------
# Polymorphism in Python
# ------------------------------

# Polymorphism → "One name, many forms"
# Allows same function/method/operator to behave differently

# ---------------------------------
# 1. Compile-Time Polymorphism
# (Method Overloading in other langs)
# ---------------------------------
# Python does NOT support true method overloading
# Achieved using:
#   - Default arguments
#   - *args / **kwargs

class MathOperations:
    def add(self, a=0, b=0, c=0):
        return a + b + c

# obj.add(5)        -> 5
# obj.add(5,10)     -> 15
# obj.add(5,10,20)  -> 35

# ---------------------------------
# 2. Runtime Polymorphism
# (Method Overriding)
# ---------------------------------
# Child class redefines method of parent class
# Decided at runtime → which version runs depends on object

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

# For loop shows polymorphism:
# Dog().sound() -> Dog barks
# Cat().sound() -> Cat meows
# Animal().sound() -> Animal makes sound

# ---------------------------------
# 3. Operator Overloading
# ---------------------------------
# Same operator works differently depending on type
# Example: + works for int (addition) and str (concatenation)

print(5 + 10)       # 15 (int addition)
print("Hi " + "Py") # Hi Py (string concatenation)


print("_"*100)

# Example of Runtime Polymorphism (Method Overriding)

class SBI:
    def rate_of_interest(self):   # same method name
        return 8                  # SBI's own implementation

class HDFC:
    def rate_of_interest(self):   # same method name
        return 10                 # HDFC's own implementation

class KOTAK:
    def rate_of_interest(self):   # same method name
        return 11                 # KOTAK's own implementation

# Objects of different banks
s = SBI()
h = HDFC()
k = KOTAK()

# Polymorphism in action
for bank in (s, h, k):
    # Method behaves differently depending on the object
    print(bank.__class__.__name__, "ROI:", bank.rate_of_interest())
