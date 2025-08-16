# List comprehension
# Create a new list with squared values from my_list

my_list = [2,3,4,5,6,7]
squared_list = [val**2 for val in my_list]

# Print the squared_list
print(squared_list)

# -------------------------------------------------

# Create a new list with even numbers from my_list
even_list = [var for var in my_list if var%2==0]

# Print the even list
print(even_list)

# ---------------------------------------------------------------------------------------------------------------------
# Set comprehension
# Create a set containing numbers from 1 to 9
numbers = {x for x in range(1,100)}

# Print the numbers set
print(numbers)

# ----------------------------------------------------

# Create a set of even numbers from 1 to 10
even_numbers = [x for x in range(1,11) if x%2 == 0]

# Print the even numbers set
print(even_numbers)

# ---------------------------------------------------------------------------------------------------------------------
# Dictionary comprehension
# Create a dictionary with numbers and their squares
d = {num:num*num for num in range(1,10)}

# print the dictionary
print(d)

# ----------------------------------------------------
# Create a dictionary of squares for numbers from 1 to 5
squares_dict = {x: x**2 for x in range(10,20)}
print(squares_dict)
