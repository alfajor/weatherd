import os
import requests
import re
import json 
from dotenv import load_dotenv

load_dotenv()

ip_token = os.environ.get('IP_INFO_TOKEN')
open_weather_token = os.environ.get('OPEN_WEATHER_TOKEN')

## Set up API key here
## https://openweathermap.org/api

def get_data_endpoint():
    target_city = get_location_info('city')
    target_country = get_location_info('country')

    us_unit = 'imperial'
    world_unit = 'metric' 

    search_value = re.search("US", target_country)
    unit = us_unit if search_value else world_unit
    
    res = requests.get('http://api.openweathermap.org/data/2.5/weather?q={},{}&units={}&appid={}'.format(str(target_city), str(target_country), str(unit), open_weather_token))
    output = res.json()

    return output

def get_weather():
    source_data = get_data_endpoint()

    name = source_data['name']
    temp = source_data['main']['temp']
    feels_like = source_data['main']['feels_like']
    temp_max = source_data['main']['temp_max']
    temp_min = source_data['main']['temp_min']
    description = ''

    for data in source_data['weather']:
        description = data['description']
       
    weather_overview = 'The current temperature in {} is {} but feels like {}'.format(name, temp, feels_like) 
    more_info = 'The high is {} with a low of {} and {}'.format(temp_max, temp_min, description)

    return weather_overview + '\n' + more_info


def get_location_info(location_type):
    ip_endpoint = 'https://ipinfo.io/{}?token={}'.format(location_type, ip_token)
    result = requests.get(ip_endpoint)

    return result.text
