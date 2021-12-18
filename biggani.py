
import os
import json
import time
from datetime import date, timedelta
from bs4 import BeautifulSoup
import requests

# from io import open

newspaper_base_url = 'http://biggani.org/'

output_result = []
data = []
exceptions = 0

for index in range(1, 100):
    for j in range(40):
        if j == 0:
            url = newspaper_base_url + "?cat=25&paged=" + str(index)
        elif j == 1:
            url = newspaper_base_url + "?cat=893&paged=" + str(index)
        elif j == 2:
            url = newspaper_base_url + "?cat=28&paged=" + str(index)
        elif j == 3:
            url = newspaper_base_url + "?cat=30&paged=" + str(index)
        elif j == 4:
            url = newspaper_base_url + "?cat=32&paged=" + str(index)
        elif j == 5:
            url = newspaper_base_url + "?cat=44&paged=" + str(index)
        elif j == 6:
            url = newspaper_base_url + "?cat=47&paged=" + str(index)
        elif j == 7:
            url = newspaper_base_url + "?cat=24&paged=" + str(index)
        elif j == 8:
            url = newspaper_base_url + "?cat=17&paged=" + str(index)
        elif j == 9:
            url = newspaper_base_url + "?cat=866&paged=" + str(index)
        elif j == 10:
            url = newspaper_base_url + "?cat=35&paged=" + str(index)
        elif j == 11:
            url = newspaper_base_url + "?cat=27&paged=" + str(index)
        elif j == 12:
            url = newspaper_base_url + "?cat=914&paged=" + str(index)
        elif j == 13:
            url = newspaper_base_url + "?cat=14&paged=" + str(index)
        elif j == 14: