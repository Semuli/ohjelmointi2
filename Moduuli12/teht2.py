import requests
import json

apikey = "fddeb8f21dc4294d060800e064af7344"

paikkakunta = input("Kerro paikkakunta:")

haku = "https://api.openweathermap.org/data/2.5/weather?q=" + paikkakunta + "&appid=" + apikey + "&units=metric&lang=Fi"

try:
    vastaus = requests.get(haku)
    if vastaus.status_code==200:
        json_vastaus = vastaus.json()
        print(f'{str.capitalize(paikkakunta)} sää: {json_vastaus["weather"][0]["description"]}\nlämpötila: {json_vastaus["main"]["temp"]}C')
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")


