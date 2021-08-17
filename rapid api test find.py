import requests

url = "https://community-open-weather-map.p.rapidapi.com/find"
querystring = {"q":"paris","cnt":"1","mode":"null","lon":"0","type":"link, accurate","lat":"0","units":"metric"}
headers = {
    'x-rapidapi-key': "55e936b370msh6c7e5a380d1dd15p15cf3ejsn8a74180a1b37",
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }
response = requests.request("GET", url, headers=headers, params=querystring)
print(type(response.text))
print(response.text)
