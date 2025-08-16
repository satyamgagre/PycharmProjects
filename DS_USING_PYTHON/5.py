def my_func(a,b):
    return a * b
print(my_func(10,13))

#-------------------------------------------------
def my_func(a,b,c):
    return a * b + c
print(my_func(10,13,15))

# ---------------------------------------------------
def marks(maths, science, english):
    return (maths + science + english )/3

# defaults ways to passing ways
print(marks(96,85,80))

# calling function with keywords
print(marks(maths=85, science=81, english=95))

# calling function, by changing the position of arguments with keywords
print(marks(english=80, science=90, maths=97))

# ---------------------------------------------------

#pass by object reference
def modify_list(my_list):
    my_list.append(4)
    my_list[0] = 100

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
modify_list(numbers)

print(numbers)
