from collections import  deque

#stack method
print("Stack Method using deque")
numbers = deque()
print(numbers)

#adding items push
numbers.append(13)
numbers.append(45)
numbers.append(136)
numbers.append(143)

print(numbers)

#Removing items using pop method
numbers.pop()
print(numbers)

print("Queue Method using deque")
names = deque()
print(names)

#adding items using enqueue
names.append("Rohit")
names.append("Shikhar")
names.append("Virat")
names.append("Shreyash")
names.append("Dhoni")
names.append("Jadeja")
names.append("Ashwin")
names.append("Bhumrah")
names.append("Bhuvneshwar")
names.append("Kuldeep")
names.append("Shami")
print("Playing XI of Indian Cricket Team")
print(names)

# Removing items using deque
names.popleft()
print(names)