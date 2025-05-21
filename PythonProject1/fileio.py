s = "Satya is a bad boy"

with open("myfile.txt", "w") as myfile:
    myfile.write(s)

#     with function we dont need to close file
with open("myfile.txt", "r") as myfile:
    content = myfile.read()
    print("THE CONTENT OF A FILE IS...")
    print(content)

