# Date class example
from datetime import date

# Create a specific date
mydate = date(year=2003, month=10, day=1)
print("Date is:", mydate)

# Get today's date
today = date.today()
print("Current date:", today)

# Get current year
print("Current year:", today.year)

# Get current month
print("Current month:", today.month)

# Get current day
print("Current day:", today.day)

print("_"*100)

# Time class example
from datetime import time
# Create a time object with the specified hour, minute and ,second
mytime = time(hour=12, minute=34, second=56)

# print the time object
print("Time is : ",mytime)

# Create a time object with a specified minute
mytime = time(minute=34)

# print the time object
print("Time is :", mytime)

# Create a time object with the specified hour, minute and ,second
mytime = time(hour=1, minute=2, second=3)

# print the time object
print("Time is : ",mytime)

# Display the hour
print(mytime.hour)

# Display the minute
print(mytime.minute)

# Display the second
print(mytime.second)