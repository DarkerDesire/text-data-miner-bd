
import os
import json
import time
from datetime import date, timedelta
from bs4 import BeautifulSoup
import requests

# from io import open

newspaper_base_url = 'https://www.bd-pratidin.com/'

output_result = []
data = []
exceptions = 0

for i in range(100):
    index = i * 12

    for j in range(28):
        if j == 0:
            url = newspaper_base_url + "national/" + str(index)
        elif j == 1:
            url = newspaper_base_url + "city-news/" + str(index)
        elif j == 2:
            url = newspaper_base_url + "country/" + str(index)
        elif j == 3:
            url = newspaper_base_url + "international-news/" + str(index)
        elif j == 4:
            url = newspaper_base_url + "entertainment/" + str(index)
        elif j == 5:
            url = newspaper_base_url + "sports/" + str(index)
        elif j == 6:
            url = newspaper_base_url + "mixter/" + str(index)
        elif j == 7:
            url = newspaper_base_url + "chayer-desh/" + str(index)
        elif j == 8:
            url = newspaper_base_url + "probash-potro/" + str(index)