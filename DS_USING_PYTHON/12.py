# Lets take an example to understand string formatting
x = 10
y = 3
z = x/y

# lets print the output
print(z)

# lets try string formatting
print("The output is {0:.2f}".format(z))

# lets take one more example of string formatting
name = "Satya"
age = 22

# lets try to print values of name and age
print("My name  is {}. and I'm {} years old.".format(name, age))

#----------------------------------------------------------------------------------------
# User Input function
# by default user input function takes only string datatype
name = input("enter your name:")

# lets print the ouput
print("My name is :", name)

# lets take an example for the input function to enter int and float values
# lets take an integer input
x = int(input("Enter an Integer: "))

# lets take a float inpyt
y = float(input("Enter a float: "))

# lets calculate the product of two variables
z = x*y

# print the output
print("The product of {} and {} is {}.".format(x, y, z))