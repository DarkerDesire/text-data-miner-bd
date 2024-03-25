
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