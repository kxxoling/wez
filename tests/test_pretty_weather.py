# coding: utf-8
from __future__ import print_function
import unittest

from wez.pretty_weather import PrettyWeather
import wez.pretty_weather as pw


class PrettyWeatherTest(unittest.TestCase):
    def test_weather_property(self):
        self.assertEqual(pw.sunny, PrettyWeather(113).weather)
        self.assertEqual(pw.unknown, PrettyWeather('unknown').weather)
        self.assertEqual(pw.unknown, PrettyWeather(007).weather)

