# coding: utf-8

import os
import requests


API_URL = 'https://api.worldweatheronline.com/free/v2/weather.ashx'
DEFAULT_PARAM = dict(
    format='json',
    num_of_days=3,
    tp=3,
    lang='',
)

API_KEY = os.environ.get('WWO_API_KEY')


def get_weather_info(q):
    """
    Get the weather status of ``q``.
    :param q: query word. This can be the English name of a place or an IP address, etc.
    :return:
    """
    params = dict()
    api_url = API_URL
    params.update(DEFAULT_PARAM)
    params.update(dict(q=q, key=API_KEY))

    weather_info = requests.get(api_url, params=params).json()
    return weather_info


def gen_weather_board(datefmt):
    board =\
        [ "                                                       ┌─────────────┐                                                       ",
          "┌──────────────────────────────┬───────────────────────" + datefmt + "───────────────────────┬──────────────────────────────┐",
          "│           Morning            │             Noon      └──────┬──────┘    Evening            │            Night             │",
		  "├──────────────────────────────┼──────────────────────────────┼──────────────────────────────┼──────────────────────────────┤",
        ]\
        + []\
        +["└──────────────────────────────┴──────────────────────────────┴──────────────────────────────┴──────────────────────────────┘",]

    return '\n'.join(board)
