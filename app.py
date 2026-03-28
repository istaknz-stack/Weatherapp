import requests

API_KEY = "e74abae1a9d5c6b382ab0aeea0c7ec80"

city = input("Enter city name: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if data["cod"] != 200:
    print("City not found!")
else:
    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]

    print(f"\nWeather in {city}:")
    print(f"Temperature: {temp}°C")
    print(f"Condition: {weather}")