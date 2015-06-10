# coding: utf-8
import unittest
from os import getenv
from requests.models import json
from wez.main import get_weather_info


class APITest(unittest.TestCase):
    @unittest.skipIf(not getenv("TEST_API"), 'Skip this if TEST_API not setting.')
    def test_get_weather_info(self):
        weather_info = get_weather_info()
        self.assertIsInstance(weather_info, json)
