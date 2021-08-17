import requests
import csv
import os
import json

#the interface for all the classes
class IWeather:  
    def find_weather_in_city(cityname: str, count: str, mode: str, lon: str, type1: str, lat: str, units: str):
        """ sets the parameters for the querystring and makes the api call"""

#a class that takes all the parameters and sends them to the api
class RapidWeatherAPI(IWeather):
    def find_weather_in_city(cityname: str, count: str, mode: str, lon: str, type1: str, lat: str, units: str):
        url = "https://" + os.environ["RapidUrl"] + "/find"
        querystring = {"q":cityname,"cnt":count,"mode": mode,"lon":lon,"type":type1,"lat":lat,"units":units}
        headers = {
            'x-rapidapi-key': os.environ["RapidKey"],
            'x-rapidapi-host': os.environ["RapidUrl"]
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        jason_string = response.text 
        jason_string = json.loads(jason_string)
        print(jason_string)

#a class that takes all the parameters and sends them to a mock data base      
class MockWeatherAPI(IWeather):
    def find_weather_in_city(cityname: str, count: str, mode: str, lon: str, type1: str, lat: str, units: str):
        try:
            f = open(f'{cityname}_{count}.json')
        except:
            try:
                f = open(f'{cityname}.json')
            except:
                try:
                    f = open('london.json')
                except:
                    return(False)
        data = json.load(f)
        #data = json.dumps(data)
        return(data)

#decadids wich of the class to use        
class WeatherWarpper(IWeather):
    def find_weather_in_city(cityname: str, count: str, mode: str, lon: str, type1: str, lat: str, units: str):
        if os.environ["UseRapidApi"] == 'true':
            return(RapidWeatherAPI.find_weather_in_city(cityname,count,mode,lon,type1,lat,units))
        else:
            return(MockWeatherAPI.find_weather_in_city(cityname,count,mode,lon,type1,lat,units))


#WeatherWarpper.find_weather_in_city('paris','1','null','0','link, accurate','0','metric')
RapidWeatherAPI.find_weather_in_city('tokyo','1','null','0','link, accurate','0','metric')
#MockWeatherAPI.find_weather_in_city('paris','1','','','','','')
