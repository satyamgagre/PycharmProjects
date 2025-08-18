import re

s1 = "I love watching movies. The time is 10pm."

# \A → matches only at the start of the string
print("Using \\A:", re.findall(r"\AI", s1))       # Matches 'I'
print("Using \\A:", re.findall(r"\AThe", s1))     # Won’t match because string starts with "I"

# \B → matches where there is no word boundary
print("Using \\B:", re.findall(r"\Bove", s1))     # Matches 'ove' in 'love' (not at word boundary)

# \d → matches any digit
print("Using \\d:", re.findall(r"\d", s1))        # ['1', '0']

# \D → matches any non-digit
print("Using \\D:", re.findall(r"\D", s1))        # Every non-digit character

# \s → matches any whitespace
print("Using \\s:", re.findall(r"\s", s1))        # [' ', ' ', ' ', ' ', ' ', ' ', ' ']
