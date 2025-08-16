# filter() function

# Define a function to filter even numbers
def is_even(num):
    return num % 2 == 0

# create a list of numbers
numbers = [1,2,3,4,5,6,7,8,9,10]

# Use filter() to filter even numbers from the list
filtered_numbers = filter(is_even, numbers)

# Convert the filtered result into a list
even_numbers = list(filtered_numbers)

# Let's print the output
print(even_numbers)

# -----------------------------------------------------------------------------------------------
# Filter function examples

# create a list named "score"
score = [75,34,64,33,86,54,35,75,46,46,65,35,56,47,86,96]

# defining a function to check if the score is greater than 50
def score_check(score):
    if score > 50:
        return True
    else:
        return False

# Let's apply the filter to the list
students_passed = filter(score_check, score)

# Let's print the output
for i in students_passed:
    print(i)

# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------
# map() function
# Square each element in a list

# Let's take a list named as a numbers
numbers = [1,2,3,4,5,6,7,8,9,10]

# Let's create a function named as square
def square(numbers):
    return numbers**2

# Let's map the function to the list named as numbers
squared_numbers = list(map(square, numbers))

# Let's print the value
print(squared_numbers)

# --------------------------------------------------------------------------------------------------------------------
# Convert a list of temperature from Celsius to Fahrenheit

# Let's create a list of temperature in celcius
celcius_temperatures = [25,30,15,10]

# Let's create a function called convertor , which can convert the celcius temperature into fahreintheit temperature
def convertor(temp):
    temp = (temp - 32) * 5/9
    return temp

# Let's map the convertor function in the celsius temperatures list.
fahrenheit_temperatures = list(map(convertor, celcius_temperatures))

# Let's print the output
print(fahrenheit_temperatures)

# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------
# Zip() function
# We have two lists, First list contains the name, and second list contains the ages.
names = ['Rohit','Shikhar','Virat','Suresh','Dhoni','Jadeja','Bhuvaneshwar','Bhumrah','Kuldeep','Shami','Chahal']
ages = [36, 37, 35, 37, 43, 35, 34, 31, 29, 34, 34]

# Zip the list together
combined = zip(names, ages)

# Iterate over the combined iterator
print("Playing XI of Indian Cricket Team:")
for name, age in combined:
    print(name, age)

# --------------------------------------------------------------------------------------------------------------------
# Let's take a list of students having the student's name and age
students = [('Alice',25),('Bob',26),('Charlie',28)]

# Unzip the tuples
names, ages = zip(*students)

# Iterate correctly
print(names, ages)
