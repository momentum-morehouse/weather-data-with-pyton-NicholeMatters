import requests
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors
print('Done!')

#Tennessee State 36.1668° N, 86.8276° W
#Georgia State 32.1656° N, 82.9001° W
#UGA 33.9480° N, 83.3773° W
#Morehouse 33.7473° N, 84.4155° W
#Spelman 33.7464° N, 84.4121° W
#Clark Atlanta 33.7516° N, 84.4112° W
#Howard 38.9227° N, 77.0194° W
#Tuskegee 32.4308° N, 85.7073° W
#FAMU 30.4269° N, 84.2851° W
#Grambling
#Syndey, AU 33.8688° S, 151.2093° E

place_list = [(36.1668, -86.8276, 'Tennessee State'), (32.1656, 82.9001, 'Georgia State'), (33.9480, 83.377, 'UGA'), (33.7473, 84.4155, 'Morehouse'), (42.30260171891152, -71.17609710203855, 'Spelman'), (33.7516, 84.4112, 'Clark Atlanta'), (38.9227, 77.0194, 'Howard'), (32.4308, 85.7073, 'Tuskegee'), (30.4269, 84.2851, 'FAMU'), (33.8688, 151.2093, 'Syndey, AU')]

class Places:
  def __init__(self, name, lat, long):
    self.name = name
    self.lat = lat
    self.long = long

  def __str__(self):
    return(f'{self.name} latitude: {self.lat} longitude: {self.long} ')

def create_list(list):
    places = []
    for city in list:
      place = Places(city[0], city[1], city[2])
      places.append(place)
    return places
    


places = create_list(place_list) 

print(places)    

class Weather_Report:
  # def __init__(self, latitude, longiture, temperature):
  #   self.latitude = lat
  #   self.longitude = log
  #   self.temperature = temp
  pass

  # def __str__(): 
  #   return(f'{self.place} Feels Like: {self.feels}f Current Temp: {self.long}f')

def weather(locations):
  # get lats and longs from tuples
  weather_data = ()
  for location in locations:
      url = 'https://developer.climacell.co/v3/reference#get-realtime'

      payload = {
        "apikey":"FO5TGSFTVGcY57KGMTBqFGbr3131XBsN",
        "latitude": latitude,
        "longiture": longiture,
        "fields": ["feels_like", "temp", "precipitation", "wind_speed"],
        "unit_system":"us", 
        }

  response = requests.get(url, params=payload).json()
  weather_data[location[2]] = response["temp"] ["value"]
  
    #response = requests.request("GET", url)
  
#get_weather_data(42.30260171891152, -71.17609710203855, "temperature")

#get_weather_data(23.0506249, -82.4730905, "temp")