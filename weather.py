import requests
import matplotlib
#print ("libraries imported")


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


place_list = [('Tennessee State', 36.1668, -86.8276), ('Georgia State', 32.1656, 82.9001 ), ('UGA', 33.9480, 83.377), ('Morehouse', 33.7473, 84.4155), ('Spelman', 42.30260171891152, -71.17609710203855), ('Clark Atlanta', 33.7516, 84.4112), ('Howard', 38.9227, 77.0194), ('Tuskegee', 32.4308, 85.7073), ('FAMU', 30.4269, 84.2851), ('Syndey, AU', 33.8688, 151.2093)]

class Place:
  def __init__(self, name, lat, long):
    self.name = name
    self.lat = lat
    self.long = long

  def __str__(self):
    return(f'{self.name} latitude: {self.lat} longitude: {self.long} ')

def create_list(list):
    places = []
    for city in list:
      place = Place(city[0], city[1], city[2])
      places.append(place)
    return places
    


places = create_list(place_list) 

print(places)    

class Weather_Report:
  def __init__(self, place, feels, temp):
    self.place = location
    self.feels = feels_like
    self.temp = temperature
    self.rain = rain
    self.wind = wind_gust

  def __str__(): 
    return(f'{self.place} Feels Like: {self.feels}f Current Temp: {self.long}f')

def get_weather_data(lat, lon):
  # get lats and longs from tuples
 
    url = "https://api.climacell.co/v3/weather/forecast/hourly"

    payload = { "apikey": "FO5TGSFTVGcY57KGMTBqFGbr3131XBsN",
      "lat": lat, 
      "lon": lon,
      "fields": ["feels_like", "temp", "precipitation", "wind_gust"],
      "unit_system":"us", 
      }

    response = requests.get(url, params=payload).json()

    #response = requests.request("GET", url)
  
get_weather_data(42.30260171891152, -71.17609710203855)

