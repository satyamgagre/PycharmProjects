# Pass Statement
# 'pass' is a placeholder that does nothing
for i in range(1, 10):
    pass   # This loop does nothing
print("~" * 100)


# Break Statement
# 'break' exits the loop completely
for i in range(10):
    print(i)  # print the values of i
    if i == 8:
        break   # stop the loop when i == 8
print("~" * 100)


# Continue Statement
# 'continue' skips the current iteration and moves to the next
for q in range(10):
    if q == 8:
        continue   # skip printing when q == 8
    print(q)
