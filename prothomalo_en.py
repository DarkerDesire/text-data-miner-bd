
import os
import json
import time
from datetime import date, timedelta
from bs4 import BeautifulSoup
import requests

newspaper_base_url = 'https://en.prothomalo.com/'
newspaper_archive_base_url = 'https://en.prothomalo.com/archive/'

start_date = date(2019, 8, 9)
end_date = date.today()
delta = end_date - start_date
output_result = []
data = []
exceptions = 0

for i in range(delta.days + 1):
    date_str = start_date + timedelta(days=i)
    print(date_str)
    index = 0
    output_dir = './{}/{}/{}/en'.format(date_str.year, date_str.month, date_str.day)
    raw_output_dir = '../' + "Raw" + '/' + "Prothom_Alo.com" + '/' + output_dir
    try:
        os.makedirs(output_dir)
    except OSError:
        pass

    try:
        os.makedirs(raw_output_dir)
    except OSError:
        pass

    url = newspaper_archive_base_url + str(date_str)
    archive_soup = requests.get(url)
    soup = BeautifulSoup(archive_soup.content, "html.parser")
    all_links = soup.find_all("a", attrs={"class": ""})
    page_links_length = len(all_links)

    if page_links_length == 0:
        break
    else:
        for link in all_links:
            link_separator = link.get('href').split('/')
            link_separator_len = len(link_separator)
            if link_separator_len != 5: continue
            link = link_separator[1] + "/" + link_separator[2] + "/" + link_separator[3] + link_separator[4]
            output_file_name = 'en_{}{}.txt'.format(link_separator[2], link_separator[3])
            article_url = newspaper_base_url + link
            print(article_url)
            try:
                article_data = requests.get(article_url)