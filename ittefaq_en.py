
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
                url = newspaper_base_url + "international/page/" + str(i + 1)
            else:
                url = "none"
        if j == 3:
            if max_business_pages >= i + 1:
                url = newspaper_base_url + "business/page/" + str(i + 1)
            else:
                url = "none"
        if j == 4:
            if max_editorial_oped_pages >= i + 1:
                url = newspaper_base_url + "editorial-oped/page/" + str(i + 1)
            else:
                url = "none"
        if j == 5:
            if max_sports_pages >= i + 1:
                url = newspaper_base_url + "sports/page/" + str(i + 1)
            else:
                url = "none"
        if j == 6:
            if max_sci_tech_pages >= i + 1:
                url = newspaper_base_url + "sci-tech/page/" + str(i + 1)
            else:
                url = "none"
        if j == 7:
            if max_culture_pages >= i + 1:
                url = newspaper_base_url + "culture/page/" + str(i + 1)
            else:
                url = "none"
        if not ("none" in url):
            print('\n' + url)

            archive_soup = ""
            try:
                archive_soup = requests.get(url, proxies={"http": proxy, "https": proxy})
            except:
                stuck = 1

            while stuck == 1:
                time.sleep(10)
                try:
                    archive_soup = requests.get(url)
                    stuck = 0
                except:
                    stuck = 1

            soup = BeautifulSoup(archive_soup.content, "html.parser")
            all_links = soup.find_all("a", attrs={"class": "read-more-link"})
            page_links_length = len(all_links)
