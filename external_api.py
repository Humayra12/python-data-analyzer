import requests
OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"
def fetch_hourly_temperature(lat, lon, timezone="America/New_York"):
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m",
        "forecast_days": 1,
        "timezone": timezone,
    }
    response = requests.get(OPEN_METEO_URL, params=params)
    data = response.json()

    times = data.get("hourly", {}).get("time", [])
    temperatures = data.get("hourly", {}).get("temperature_2m", [])

    return times, temperatures



