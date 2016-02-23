import unittest

from ..weather import get_current_weather


class WeatherTestCase(unittest.TestCase):

    def test_get_current_weather_with_ip(self):
        weather_conditions = get_current_weather(ip='1.1.1.1')
        self.assertEqual(5, len(weather_conditions.split('\n')))

    def test_get_current_weather_no_ip(self):
        weather_conditions = get_current_weather()
        self.assertEqual(5, len(weather_conditions.split('\n')))

    def test_get_current_weather_imperial(self):
        weather_conditions = get_current_weather(units='imperial')
        self.assertEqual(5, len(weather_conditions.split('\n')))
