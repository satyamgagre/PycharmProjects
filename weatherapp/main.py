import requests
import pyttsx3
while(True):
    city = input("Enter your city name: \n")

    if city.lower() == "exit":
        goodbye_msg = "Thank you for using the weather speaker. Goodbye!"
        print(goodbye_msg)
        engine.say(goodbye_msg)
        engine.runAndWait()
        break


    api_key = "22462277636764dff6c100ca3e638503"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        message = f"The current temperature of city {city} is {temperature} degree celsius"

        print(message)

        engine = pyttsx3.init()
        engine.say(message)
        engine.runAndWait()

    else:
        error_msg = "Sorry, I couldn't find the weather for that city. Please check the city name or your Api key."
        print(error_msg)

        engine = pyttsx3.init()
        engine.say(error_msg)
        engine.runAndWait()
