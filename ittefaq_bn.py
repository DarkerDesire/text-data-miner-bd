import os
import json
import time
from datetime import date, timedelta
from bs4 import BeautifulSoup
import requests

newspaper_base_url = 'https://www.ittefaq.com.bd/'
newspaper_archive_base_url = 'https://www.ittefaq.com.bd/archives/'

# start_date = date(2019,  4, 30)
# end_date   = date.today()
start_date = date(2019, 4, 30)
end_date = date.today()
delta = end_date - start_date
output_result = []
data = []

for i in range(delta.days + 1):
    date_str = start_date + timedelta(days=i)

    month = str(date_str.month)
    day = str(date_str.day)
    if date_str.month < 10: month = "0" + month
    if date_str.day < 10:   day = "0" + day

    output_dir = './{}/{}/{}/bn'.format(date_str.year, date_str.month, date_str.day)
    raw_output_dir = '../' + "Raw" + '/' + "Ittefaq.com" + '/' + output_dir

    try:
        os.makedirs(output_dir)
    except OSError:
        pass

    try:
        os.makedirs(raw_output_dir)
    except OSError:
        pass

    url = newspaper_archive_base_url + 'online-edition/{}/{}/{}'.format(date_str.year, month, day)
    print(date_str)
    print("online-edition")

    # url = newspaper_archive_base_url + 'print-edition/{}/{}/{}'.format(date_str.year, month , day)
    # print(date_str)
    # print("print-edition")
    with open("bn_log.txt", 'a', encoding='utf8') as file:
        file.write(str(date_str) + ' ' + "online-edition" + '\n')

    try:
        archive_soup = requests.get(url)
    except:
        print("No response