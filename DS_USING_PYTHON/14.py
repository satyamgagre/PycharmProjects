import re

# -------------------------
# 1. findall()
# -------------------------
txt1 = "cat bat mat rat"
print("findall() Example:")
result1 = re.findall("[a-z]at", txt1)
print(result1)   # ['cat', 'bat', 'mat', 'rat']
print("-" * 50)

# -------------------------
# 2. search()
# -------------------------
txt2 = "I love Python programming"
print("search() Example:")
result2 = re.search("Python", txt2)
if result2:
    print("Matched:", result2.group())   # Python
    print("Start Index:", result2.start())  # 7
    print("End Index:", result2.end())      # 13
print("-" * 50)

# -------------------------
# 3. sub()
# -------------------------
txt3 = "I love Java. Java is popular."
print("sub() Example:")
result3 = re.sub("Java", "Python", txt3)
print(result3)   # I love Python. Python is popular.
print("-" * 50)

# -------------------------
# 4. split()
# -------------------------
txt4 = "apple, orange; banana: mango"
print("split() Example:")
result4 = re.split("[,;:]", txt4)
print(result4)   # ['apple', ' orange', ' banana', ' mango']
print("-" * 50)
