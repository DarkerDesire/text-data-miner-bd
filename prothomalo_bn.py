
import os
import json
import time
from datetime import date, timedelta
from bs4 import BeautifulSoup
import requests

newspaper_base_url = 'http://www.prothom-alo.com/'
newspaper_archive_base_url = 'http://www.prothom-alo.com/archive/'

# start_date = date(2017, 10, 12)
# end_date = date(2018, 9, 11)
start_date = date(2018, 9, 12)
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
    raw_output_dir = '../' + "Raw" + '/' + "Prothom_Alo.com" + '/' + output_dir
    try:
        os.makedirs(output_dir)
    except OSError:
        pass
    try:
        os.makedirs(raw_output_dir)
    except OSError:
        pass

    while (True):
        index = index + 1
        url = newspaper_archive_base_url + str(date_str) + '?edition=all&page=' + str(index)
        try:
            archive_soup = requests.get(url)
        except:
            print("No response for links in archive,trying to reconnect")
            time.sleep(2)
            continue
        soup = BeautifulSoup(archive_soup.content, "html.parser")
        all_links = soup.find_all("a", attrs={"class": "link_overlay"})
        page_links_length = len(all_links)
