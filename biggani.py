
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