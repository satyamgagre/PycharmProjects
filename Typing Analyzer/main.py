from time import *
import random as r

# Function to calculate typing mistakes
def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except:
            error += 1
    return error

# Function to calculate typing speed
def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay, 2)
    speed = len(userinput) / time_R
    return round(speed)

# Typing test paragraphs
test = [
    "The quick brown fox jumps over the lazy dog. This sentence contains every letter of the alphabet and is often used to test typing skills. To improve your typing speed, it's important to focus on accuracy first. As your fingers become more familiar with the keyboard, speed will naturally increase. Practice regularly, maintain proper posture, and avoid looking at the keys. Consistency and patience are key to becoming a faster and more accurate typist.",
    "Typing is a fundamental skill in the digital age, useful in nearly every profession. Developing fast and accurate typing abilities can save time and boost productivity. Whether you're writing emails, coding, or creating documents, efficient typing helps you work smarter. Remember to use all your fingers and keep your eyes on the screen instead of the keyboard. With practice and determination, anyone can become a proficient typist.",
    "Modern technology has changed the way we communicate, work, and learn. From smartphones to cloud computing, digital tools have become a part of our daily lives. Typing efficiently on a keyboard is now more important than ever. It allows us to keep up with fast-paced environments, whether in school, at work, or in personal projects. With consistent effort and the right technique, anyone can master the skill of fast typing."
]

# Choose a random paragraph for the test
test1 = r.choice(test)

# Display the typing test
print("*****     TYPING ANALYZER     *****")
print()
print(test1)
print()

# Record typing time
time_1 = time()
test_input = input("Enter: ")
time_2 = time()

# Show results
print("\n*****     RESULT     *****")
print("Speed :", speed_time(time_1, time_2, test_input), "w/sec")
print("Errors:", mistake(test1, test_input))
