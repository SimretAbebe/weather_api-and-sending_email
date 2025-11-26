import requests

API_KEY = "ca7f1d93176e2d4a6dae646c38f816a8"

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name : ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15 , 2)

    print("Temprature is:" ,  temperature , "celsius")
    print("Weather:" , weather)


else:
    print("An error occurred.")