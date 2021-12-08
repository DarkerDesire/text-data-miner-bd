
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
        elif j == 9:
            url = newspaper_base_url + "campus-online/" + str(index)
        elif j == 10:
            url = newspaper_base_url + "facebook/" + str(index)
        elif j == 11:
            url = newspaper_base_url + "islam/" + str(index)
        elif j == 12:
            url = newspaper_base_url + "minister-spake/" + str(index)
        elif j == 13:
            url = newspaper_base_url + "corporate-corner/" + str(index)
        elif j == 14:
            url = newspaper_base_url + "chittagong-pratidin/" + str(index)
        elif j == 15:
            url = newspaper_base_url + "coronavirus/" + str(index)
        elif j == 16:
            url = newspaper_base_url + "Coronal-literature/" + str(index)
        elif j == 18:
            url = newspaper_base_url + "open-air-theater/" + str(index)
        elif j == 19:
            url = newspaper_base_url + "life/" + str(index)
        elif j == 20: