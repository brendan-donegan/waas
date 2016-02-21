import requests
import pprint

from location import (
    get_coords_from_ip,
    degrees_to_cardinal,
)


OPEN_WEATHER_MAP_API = 'http://api.openweathermap.org/data/2.5/'
APPID = 'ce790d0dfccad2d154c3778450112247'

TEMP_UNITS = {
    'metric': 'C',
    'imperial': 'F',
}
SPEED_UNITS = {
    'metric': 'Kph',
    'imperial': 'Mph',
}

DISPLAY_FORMAT = """
{location}
{conditions}
Temp: {temp}
Cloud: {cloud}
Wind: {wind}
"""


def _get_location_label(data):
    return data['name'] + ', ' +data['sys']['country']


def _get_temperature_label(data, units):
    return str(data['main']['temp']) + TEMP_UNITS[units]


def _get_conditions_label(data):
    return data['weather'][0]['description'].capitalize()


def _get_cloud_label(data):
    return str(data['clouds']['all']) + '%'


def _get_wind_label(data, units='metric'):
    return "{speed}{units}, {direction}".format(
        speed=str(data['wind']['speed']),
        units=SPEED_UNITS[units],
        direction=degrees_to_cardinal(data['wind']['deg']),
    )


def get_current_weather(ip=None, units='metric'):
    coords = get_coords_from_ip(ip)
    weather_data = _get_forecast_data(coords)
    return DISPLAY_FORMAT.format(
        location=_get_location_label(weather_data),
        conditions=_get_conditions_label(weather_data),
        temp=_get_temperature_label(weather_data, units),
        cloud=_get_cloud_label(weather_data),
        wind=_get_wind_label(weather_data, units),
    )

def _get_forecast_data(coords, units='metric'):
    params = {
        'units': units,
        'lat': coords[0],
        'lon': coords[1],
        'appid': APPID
    }
    forecast_api_url = OPEN_WEATHER_MAP_API + 'weather'
    response = requests.get(forecast_api_url, params=params)
    if not response.ok:
        return None
    return response.json()
