# Nested loops with i + j
for i in range(5):   # Outer loop (i = 0,1,2)
    print("Outer loop:", i)

    for j in range(4):  # Inner loop (j = 0,1)
        print("   Inner loop:", i + j)

print("~"*100)
# lets take an example
x = int(input("Enter a number: "))

if x > 0:
    # print a message indicationg x is positive
    print(x, "is positive")
    if x % 2 == 0 :
        # print a message indicationg x is even
        print(x, "is even")
    else:
        # print a message indicating x is odd
        print(x, "is odd")
else:
    # print a message indicating x is not possitive
    print(x, "is negative")


print("~"*100)
# Example: Nested Loops with Nested Conditional Statements

# Outer loop
for i in range(1, 4):
    print("Outer loop iteration:", i)

    # Inner loop
    for j in range(1, 4):
        print("   Inner loop iteration:", j)

        # Outer condition
        if i % 2 == 0:
            # Inner condition
            if j % 2 == 0:
                print("      Both i and j are even")
            else:
                print("      i is even, j is odd")
        else:
            if j % 2 == 0:
                print("      i is odd, j is even")
            else:
                print("      Both i and j are odd")