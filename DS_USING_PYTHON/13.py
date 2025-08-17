# Regular Expressions in Python
import re

# -------------------------
# Dot Metacharacter (.)
# -------------------------
s1, s2, s3, s4 = "cat", "cut", "cot", "pot"

print("Dot (.) Example:")
print(re.search('c.t', s1))  # matches cat
print(re.search('c.t', s2))  # matches cut
print(re.search('c.t', s3))  # matches cot
print(re.search('c.t', s4))  # None
print("-" * 50)

# -------------------------
# Caret ^ (Starts with)
# -------------------------
a1, a2, a3, a4 = "mumbai", "pune", "nashik", "amaravati"

print("Starts with ^ Example:")
print(re.search('^m', a1))  # mumbai
print(re.search('^m', a2))  # None
print(re.search('^m', a3))  # None
print(re.search('^m', a4))  # None
print("-" * 50)

# -------------------------
# Dollar $ (Ends with)
# -------------------------
b1, b2, b3, b4 = "mumbai", "pune", "nashik", "amaravati"

print("Ends with $ Example:")
print(re.search('i$', b1))  # ends with i
print(re.search('e$', b2))  # ends with e
print(re.search('n$', b3))  # None
print(re.search('i$', b4))  # ends with i
print("-" * 50)

# -------------------------
# Asterisk * (Zero or more)
# -------------------------
c1, c2, c3, c4 = "ac", "caac", "accab", "accacavb"

print("* Example:")
print(re.search('ab*c', c1))
print(re.search('ab*c', c2))
print(re.search('ab*c', c3))
print(re.search('ab*c', c4))
print("-" * 50)

# -------------------------
# Plus + (One or more)
# -------------------------
d1, d2, d3, d4 = "ac", "abc", "abbc", "cab"

print("+ Example:")
print(re.search('ab+c', d1))  # None
print(re.search('ab+c', d2))  # abc
print(re.search('ab+c', d3))  # abbc
print(re.search('ab+c', d4))  # None
print("-" * 50)

# -------------------------
# Question Mark ? (Zero or one)
# -------------------------
e1, e2, e3 = "color", "colour", "colouur"

print("? Example:")
print(re.search('colou?r', e1))  # color
print(re.search('colou?r', e2))  # colour
print(re.search('colou?r', e3))  # None
print("-" * 50)

# -------------------------
# Character set []
# -------------------------
f1 = "My name is Satyam Gagre, I live in Pune."
f2 = "I am a Engineer"
f3 = "I'll never ever give up"

print("Character Set [] Example:")
print(re.search('[in]', f1))  # matches first "n"
print(re.search('[in]', f2))  # matches "i"
print(re.search('[in]', f3))  # matches "I"
print("-" * 50)

# -------------------------
# Negated set [^ ]
# -------------------------
g1 = " I'm a an Engineer."
g2 = "i'll earn upto 50 Lacks per annum."
g3 = "I stay in Pune."
g4 = "I'll never ever give up"

print("Negated Set [^ ] Example (anything NOT a digit):")
print(re.search('[^0-9]', g1))
print(re.search('[^0-9]', g2))
print(re.search('[^0-9]', g3))
print(re.search('[^0-9]', g4))
print("-" * 50)

# -------------------------
# Pipe | (Alternation)
# -------------------------
h1, h2, h3, h4 = "I love to eat Mango", "I love to eat Litchy", "I love to eat Orange", "I love to eat Watermelon"

print("Alternation | Example:")
print(re.search('Mango|Orange', h1))  # Mango
print(re.search('Mango|Orange', h2))  # None
print(re.search('Mango|Orange', h3))  # Orange
print(re.search('Mango|Orange', h4))  # None
print("-" * 50)
