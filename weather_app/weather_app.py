import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests

# OpenWeatherMap API Key
API_KEY = "22462277636764dff6c100ca3e638503"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Colors & Fonts
TEXT_COLOR = "#011217"
FONT_TITLE = ("Merriweather", 14, "bold")
FONT_TEXT = ("Nunito Sans", 12)

# Function to get weather data
def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name.")
        return

    params = {"q": city, "appid": API_KEY, "units": "metric"}
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("Error", f"City not found: {city}")
            return

        # Extract data from JSON
        city_name = data["name"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        weather_desc = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        rain = data.get("rain", {}).get("1h", 0)

        # Update weather details
        result_label.config(
            text=f"🌍 {city_name}\n🌡️ {temp}°C (Feels like {feels_like}°C)\n"
                 f"🌤️ {weather_desc}\n💧 Humidity: {humidity}%\n"
                 f"💨 Wind: {wind_speed} m/s\n🌧️ Rain: {rain} mm",
            fg=TEXT_COLOR,
            bg="#ffffff",  # Semi-transparent effect
            font=FONT_TEXT
        )
    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "Failed to retrieve data. Check your internet connection.")

# Tkinter UI
root = tk.Tk()
root.title("DailyForecast")
root.geometry("500x300")
root.resizable(False, False)

# Load and set background image
bg_image = Image.open("images/back.jpg")  #image file
bg_image = bg_image.resize((500, 300), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)  # Make it cover entire window

# Title Label
tk.Label(root, text="DailyForecast", font=FONT_TITLE, fg=TEXT_COLOR, bg="#69bfd6").pack(pady=10)

# Entry Box
city_entry = tk.Entry(root, font=FONT_TEXT, bg="#ffffff", bd=2, relief="ridge", width=25, justify="center")
city_entry.pack(pady=5)

# Search Button
search_btn = tk.Button(root, text="Get Weather", font=FONT_TEXT, bg="#9faac3", fg="white", bd=0,
                       activebackground="#817fa0", cursor="hand2", command=get_weather)
search_btn.pack(pady=10)

# Weather Result Label
result_label = tk.Label(root, text="", font=FONT_TEXT, justify="left", bg="#ffffff")
result_label.pack(pady=10)

root.mainloop()
