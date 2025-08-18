#For loop
# Lets create a list
a = ["Pune","Mumbai","Delhi","Ahmednagar","Nashik","Beed","Ratnagiri","Kashmir","Kerala","Uttarpradesh","Maharastra"]

for city in a:
    # print each city in the list
    print(city)

print("-"*50)
# Lets create a list
s = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print("Odd numbers:")
for item in s:
    if(item%2!=0):
        print(item)

print("|"*200)

# While Loop
a = 1
while a<=5:
    # print the value of a
    print(a)
    # increment the value of a by 1 in each iteration
    a = a+1
else:
    # print the message when condition becomes fall
    print("a is no longer less than 6.")