import tkinter as tk
import requests

def get_weather():
    city = city_entry.get()

    api_key = "7101e2dae1eb935fc04ce9fcbd0a253e"
    url  = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()
        print(data)

        if data["cod"] != 200:
            result_label.config(text="❌ City not found", fg="red")
            return

        
        temp_c = data["main"]["temp"] 
        temp_f = (temp_c * 9/5) + 32

        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]

       
        if "cloud" in weather:
            icon = "☁️"
        elif "rain" in weather:
            icon = "🌧️"
        elif "clear" in weather:
            icon = "☀️"
        else:
            icon = "🌤️"

       
        result = (
            f"{icon} Weather in {city}\n\n"
            f"🌡 Temp: {temp_c:.2f}°C / {temp_f:.2f}°F\n"
            f"🌥 Condition: {weather}\n"
            f"💧 Humidity: {humidity}%"
        )

        result_label.config(text=result, fg="white")

    except:
        result_label.config(text="⚠️ Error fetching data", fg="red")



window = tk.Tk()
window.title("🌦 Weather App")
window.geometry("400x350")
window.config(bg="#1e1e1e")


tk.Label(window, text="Weather App",
         font=("Arial", 16),
         bg="#1e1e1e", fg="white").pack(pady=10)


tk.Label(window, text="Enter City Name",
         bg="#1e1e1e", fg="white").pack(pady=5)

city_entry = tk.Entry(window, font=("Arial", 12))
city_entry.pack(pady=5)


tk.Button(window, text="Get Weather",
          command=get_weather,
          bg="blue", fg="white",
          font=("Arial", 12)).pack(pady=10)


result_label = tk.Label(window, text="",
                        bg="#1e1e1e", fg="white",
                        font=("Arial", 11), justify="center")
result_label.pack(pady=20)


window.mainloop()
