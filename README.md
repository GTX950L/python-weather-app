# 🌤️ Weather Checker

Get real-time weather conditions and a 3-day forecast for any city worldwide — using a free API with no key required!

## 🚀 How to Run

```bash
python weather.py
```

**No dependencies needed!** Uses only Python's built-in `urllib` and `json` modules.

## 📖 Usage

```
🏙️  City: Shanghai
Fetching weather for 'Shanghai'...

==================================================
  🌤️   Weather for Shanghai
  📍 Shanghai, China
==================================================
  🌡️  Temperature:  22°C  (feels like 24°C)
  ☁️  Condition:     Sunny
  💧 Humidity:      65%
  💨 Wind:          12 km/h SE
  👁️  Visibility:    10 km
  ☀️  UV Index:      5
==================================================

📅  3-Day Forecast:
  2026-05-31 | Sunny          | 18°C ~ 26°C
  2026-06-01 | Partly cloudy  | 20°C ~ 28°C
  2026-06-02 | Light rain     | 19°C ~ 24°C
```

## 🛠️ Features

- ✅ Real-time weather from [wttr.in](https://wttr.in) (free, no API key)
- ✅ Temperature, humidity, wind, visibility, UV index
- ✅ 3-day forecast
- ✅ Supports city names in English and Chinese
- ✅ No external dependencies

## 📚 What I Learned

- Making HTTP requests with `urllib`
- Parsing JSON responses
- Working with nested dictionaries
- String formatting for clean output
- Error handling for network requests
- Building an interactive CLI tool
