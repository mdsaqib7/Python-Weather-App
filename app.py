import requests

api_key = '40d1ad355b8e2bf6a0ea86ab4653911e'
city_name = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=imperial&appid={api_key}"
)

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temperature = round(weather_data.json()['main']['temp'])
    print(f"The weather in {city_name} is: {weather}")
    print(f"The temperature in {city_name} is: {temperature} F degrees")
