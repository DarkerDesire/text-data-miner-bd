
import os
import json
import time
from datetime import date, timedelta
from bs4 import BeautifulSoup
import requests

newspaper_base_url = 'https://samakal.com/'
newspaper_archive_base_url = 'https://samakal.com/archive/'  # ?date=2014-01-01&page=0

start_date = date(2014, 1, 1)
end_date = date.today()
delta = end_date - start_date
output_result = []
data = []
exceptions = 0

for i in range(delta.days + 1):
    date_str = start_date + timedelta(days=i)
    print(date_str)
    output_dir = './{}/{}/{}/bn'.format(date_str.year, date_str.month, date_str.day)
    raw_output_dir = '../' + "Raw" + '/' + "Samakal" + '/' + output_dir
    try:
        os.makedirs(output_dir)
    except OSError:
        pass
    try:
        os.makedirs(raw_output_dir)
    except OSError:
        pass
    for index in range(15):
        url = newspaper_archive_base_url + '?date=' + str(date_str) + '&page=' + str(index)
        try:
            print(url)
            archive_soup = requests.get(url)
        except:
            print("No response for links in archive,trying to reconnect")
            time.sleep(2)
            continue
        soup = BeautifulSoup(archive_soup.content, "html.parser")
        all_links = soup.find_all("a", attrs={"class": "link-overlay"})
        page_links_length = len(all_links)

        if page_links_length == 0:
            break
        else:
            for link in all_links:
                article_url = link.get('href')
                link_separator = link.get('href').split('/')
                output_file_name = '{}_{}_{}_{}.txt'.format(link_separator[3], link_separator[4], link_separator[5],
                                                            link_separator[6])
                title = link_separator[6]
                title = title.replace("-", " ")
                try:
                    print(article_url)