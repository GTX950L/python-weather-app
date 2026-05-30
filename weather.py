"""
🌤️ Weather Checker
Get real-time weather for any city using the free wttr.in API.

Run: python weather.py
Dependency: None (uses only built-in urllib!)
"""

import urllib.request
import json


def get_weather(city):
    """
    Fetch weather data from wttr.in (free, no API key needed).
    Returns a dictionary with weather info.
    """
    # wttr.in provides a free JSON weather API
    url = f"https://wttr.in/{city}?format=j1"

    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))
            return data
    except urllib.error.URLError:
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def display_weather(city, data):
    """Nicely format and display weather information."""
    if data is None:
        print(f"❌ Could not fetch weather for '{city}'.")
        print("   Check your internet connection or city name.")
        return

    current = data["current_condition"][0]
    location = data["nearest_area"][0]

    # Extract data
    temp_c = current["temp_C"]
    feels_like = current["FeelsLikeC"]
    humidity = current["humidity"]
    weather_desc = current["weatherDesc"][0]["value"]
    wind_speed = current["windspeedKmph"]
    wind_dir = current["winddir16Point"]
    visibility = current["visibility"]
    uv_index = current["uvIndex"]

    country = location["country"][0]["value"]
    area = location["areaName"][0]["value"]

    print("\n" + "=" * 50)
    print(f"  🌤️   Weather for {city.title()}")
    print(f"  📍 {area}, {country}")
    print("=" * 50)
    print(f"  🌡️  Temperature:  {temp_c}°C  (feels like {feels_like}°C)")
    print(f"  ☁️  Condition:     {weather_desc}")
    print(f"  💧 Humidity:      {humidity}%")
    print(f"  💨 Wind:          {wind_speed} km/h {wind_dir}")
    print(f"  👁️  Visibility:    {visibility} km")
    print(f"  ☀️  UV Index:      {uv_index}")
    print("=" * 50)

    # Forecast for next 3 days
    print("\n📅  3-Day Forecast:")
    print("-" * 40)
    for day in data["weather"][:3]:
        date = day["date"]
        high = day["maxtempC"]
        low = day["mintempC"]
        avg = day["avgtempC"]
        desc = day["hourly"][4]["weatherDesc"][0]["value"]
        print(f"  {date} | {desc:15s} | {low}°C ~ {high}°C")


def main():
    print("=" * 50)
    print("    🌤️   Weather Checker")
    print("=" * 50)
    print("Enter a city name to get weather (type 'quit' to exit)")

    while True:
        city = input("\n🏙️  City: ").strip()

        if not city:
            continue

        if city.lower() == "quit":
            print("Goodbye! 👋")
            break

        # Support Chinese city names
        print(f"Fetching weather for '{city}'...")
        data = get_weather(city)

        if data:
            display_weather(city, data)
        else:
            print(f"❌ Could not fetch weather for '{city}'.")


if __name__ == "__main__":
    main()
