
import os
import json
import time
from datetime import date, timedelta
from bs4 import BeautifulSoup
import requests

newspaper_base_url = 'https://www.jugantor.com/'
newspaper_archive_base_url = 'https://www.jugantor.com/archive/'

# start_date = date(2017, 10, 12)
# end_date = date(2018, 9, 11)
start_date = date(2017, 12, 18)
end_date = date.today()
delta = end_date - start_date
output_result = []
data = []
exceptions = 0

for i in range(delta.days + 1):
    date_str = start_date + timedelta(days=i)
    print(date_str)
    index = 0
    output_dir = './{}/{}/{}/bn'.format(date_str.year, date_str.month, date_str.day)
    raw_output_dir = '../' + "Raw" + '/' + "Jugantor" + '/' + output_dir
    try:
        os.makedirs(output_dir)
    except OSError:
        pass
    try:
        os.makedirs(raw_output_dir)
    except OSError:
        pass

    index = index + 1
    url = newspaper_archive_base_url + str(date_str.year) + "/" + str(date_str.month) + "/" + str(date_str.day)
    try:
        archive_soup = requests.get(url)
    except:
        print("No response for links in archive,trying to reconnect")
        time.sleep(2)
        continue
    print(url)
    soup = BeautifulSoup(archive_soup.content, "html.parser")

    all_links = soup.find_all("a")
    page_links_length = len(all_links)

    if page_links_length == 0:
        break
    else:
        for link in all_links:
            article_url = link.get('href')
            link_separator = article_url.split('/')
            if len(link_separator) != 6 or link_separator[2] != "www.jugantor.com":
                continue
            if link_separator[3] == "covid-19":
                output_file_name = '{}_{}.txt'.format(link_separator[3], link_separator[4])
                title = ""
            else: