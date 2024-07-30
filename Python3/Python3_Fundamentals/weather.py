import requests
city = "Salt Lake City"

url = "http://api.weatherapi.com/v1/current.json?key=327d3cf7124f4653963141701241707&q="+city+"&aqi=no"
response = requests.get(url)

weather_json = response.json()

temp = weather_json.get("current").get("temp_f")
weather = weather_json.get("current").get("condition").get("text")

print(f"It is {temp} degrees F.")
print(f"It is currently {weather} in {city}.")
