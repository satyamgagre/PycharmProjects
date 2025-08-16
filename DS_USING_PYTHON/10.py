# Assign a value of 3 to x
x = 3

# Evaluate the expression 'x**2 + 2*x - 2'
result = eval('x**2 + 2*x - 2')

print(result)

# ------------------------------------------------------
# len() function
# create a list called numbers
numbers = [1,2,3,4,5]

# get the length of numbers list
length = len(numbers)
print(length)

# ------------------------------------------------------
# factorial() function
# lets import the maths module
import math

# lets find out the factorial of 5
fact = math.factorial(length)
print(fact)

# ------------------------------------------------------
# sort() function
# create a list called "runs"
runs = [25,89,69,105,253,175]

# sort the runs list in descending order
runs.sort(reverse=True)

# Print the sorted runs list
print(runs)

# ------------------------------------------------------
# aggregate() function
# Lets create a list
list1 = [3,5,7,9,2,1,1]

# finding the maximum value of the list
print(max(list1))

# finding the minimum value of the list
print(min(list1))

# finding the sum of all values of the list
print(sum(list1))

# ------------------------------------------------------
# Lets import the statistics module
import statistics as stat

# taking a list
list1 = [ 3,5,7,9,2,1,1]

# finding the mean value of the list
print(stat.mean(list1))

# finding the mediam of the list
print(stat.median(list1))

# finding the mode of the list
print(stat.mode(list1))