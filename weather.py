import requests

cities = ('san francisco', 'london', 'sheremetyevo', 'cherepovets')
payload = {"nTqM":"","lang=ru":""}
for city in cities:
    response = requests.get(f"https://wttr.in/{city}", params=payload)
    response.raise_for_status()

    print(response.text)

