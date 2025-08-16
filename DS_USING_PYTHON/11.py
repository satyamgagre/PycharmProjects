#String methods


# lets take a string
text = "Python is a fun!"

# lets print the length of the text
print(len(text))

# convert string to uppercase
print(text.upper())

# convert string to lowercase
print(text.lower())

# Replace a substring
print(text.replace('Python', 'Java'))


# lets take a string
text1 = "                 My Name is Satya.             "

# lets use the strip function to remove the extra spaces
print(text1.strip())

# lets take a string
text2 = "My Name ,its Satya."

# lets use the split function to split through comma
print(text2.split(","))

# Lets explore startswith and endswith function
text3 = "Hello, My name is Satya"

# lets check the output for the startswith function
print(text3.startswith("Hello"))

# lets check the output for the endswith function
print(text3.endswith("name"))

# lets explore the count function
text4 = "Hello world!"

# lets check the occurrence of "o"
print(text4.count("o"))
print(text4.count("l"))

# Lets explore the join function
text5 = "Hello" , "world!"

# lets join the string in the my_list
my_string =  ", ".join(text5)
print(my_string)