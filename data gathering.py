from Weather_Api_Test import WeatherWarpper
import datetime
import sqlite3
import os
import json

#setting up the connection to the sqlite data base
conn = sqlite3.connect('WeatherData.db')
c = conn.cursor()

# tring to create a table if one in that name doesn't exsist yet
try:
    c.execute('''CREATE TABLE WeatherDataTable(reqcity text, responsecity text, date timestamp text, temp numeric, info blob)''')
except sqlite3.OperationalError:
    pass

#setting up the parameters to send to the api
reqcityname = 'paris'
response = WeatherWarpper.find_weather_in_city(reqcityname,'1','null','0','link, accurate','0','metric')['list']

#inserts all the data to the data base in separate collums for each instance of the info resived
for information in response:
    responsename = information['name']
    temperatur = information['main']['temp']
    temperatur : float = temperatur
    c.execute(f'INSERT INTO WeatherDataTable VALUES("{reqcityname}","{responsename}","{datetime.datetime.now()}","{temperatur}","{information}")')
    #saves all the chages to the data base
    conn.commit()
    
#saves all the chages to the data base
conn.commit()

for row in c.execute('SELECT * FROM WeatherDataTable ORDER BY temp'):
        print(row)

   
#closes the connection to the data base
conn.close()


