#Using Conditional statements in Loops
# Lets create a list
number = [1,2,3,4,5,6,7,8,9,10]

for num in number:
    if num % 2 == 0:

        # Print the numbers and indiacates as a even numbers.
        print(num, "is even")

    else:
        # print the numbers and indicates as a odd numbers.
        print(num, "is odd")

print("~"*100)

# lets take an example
count = 0

while count < 10:
    # print the current value of count
    print("count", count)
    count += 1

print("~"*100)
# lets create a list
numbers = [1,2,3,4,5,6,7,8,9,10]

for  nums in numbers:
    if nums == 5:
        break #exit the loop if num is 5
    if nums % 2 == 0:
        continue #skip even numbers
    print(nums)