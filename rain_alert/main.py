import requests
import pandas

API_KEY = "bedc830d9bbe261ce7eceec272f04c18"
OWM_ENDPOINT = f"https://api.openweathermap.org/data/3.0/onecall"

parameters = {
    "lat": 50.054810,
    "lon": 19.927839,
    "exclude": "current,minutely,daily",
    "appid": API_KEY
}

# response = requests.get(OWM_ENDPOINT, params=parameters)
# response.raise_for_status()

# weather_data = response.json()
# pandas.DataFrame.from_dict(weather_data).to_json("weather_data.json")
weather_data = pandas.read_json("weather_data.json")

hourly_forecast = weather_data["hourly"][0:12]

will_rain = False
for hour in hourly_forecast:
    if hour["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    print("bring umbrella")
else:
    print("don't bring umbrella")
