
import os
import json
import time
from datetime import date, timedelta
from bs4 import BeautifulSoup
import requests
import string

# 0 - 800
# 801 - 1600
# 1601 - 4060
lim1 = 800
lim2 = 1600
lim3 = 4060

newspaper_base_url = 'https://en.ittefaq.com.bd/'

stuck = 0
max_category = 8
max_national_pages = 4060
max_politics_pages = 729
max_international_pages = 2593
max_business_pages = 527
max_editorial_oped_pages = 94
max_sports_pages = 1761
max_sci_tech_pages = 1262
max_culture_pages = 1331
myLinks = ""
output_result = []
data = []
all_url = ""
prev_j = 0
for i in range(0, lim1):
    print(str(i + 1))
    with open("en_log.txt", 'a', encoding='utf8') as file:
        file.write(str(i + 1) + '\n')
    for j in range(max_category):
        if j == 0: url = newspaper_base_url + "national/page/" + str(i + 1)
        if j == 1:
            if max_politics_pages >= i + 1:
                url = newspaper_base_url + "politics/page/" + str(i + 1)
            else:
                url = "none"
        if j == 2:
            if max_international_pages >= i + 1: