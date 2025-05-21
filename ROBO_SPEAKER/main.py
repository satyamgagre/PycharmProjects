import pyttsx3

if __name__ == '__main__':
    print("Welcome to ROBOSPEAKER 1.1 Created by Satyam.")
    while True:
        x = input("Enter what you want to speak: ")
        if x == "exit":
            break
        engine = pyttsx3.init()
        engine.say(x)
        engine.runAndWait()
