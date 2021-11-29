
#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import json
import time
from datetime import date, timedelta
from bs4 import BeautifulSoup
import requests

newspaper_base_url = 'https://www.banglanews24.com/'

for index in range(1, 25000):
    for j in range(31):
        if j == 0:
            url = newspaper_base_url + "category/জাতীয়/1?page=" + str(index)
        elif j == 1:
            url = newspaper_base_url + "category/রাজনীতি/2?page=" + str(index)
        elif j == 2:
            url = newspaper_base_url + "category/অর্থনীতি/3?page=" + str(index)
        elif j == 3:
            url = newspaper_base_url + "category/আন্তর্জাতিক/4?page=" + str(index)
        elif j == 4:
            url = newspaper_base_url + "category/খেলা/5?page=" + str(index)
        elif j == 5:
            url = newspaper_base_url + "category/বিনোদন/6?page=" + str(index)
        elif j == 6:
            url = newspaper_base_url + "category/তথ্যপ্রযুক্তি/7?page=" + str(index)
        elif j == 7:
            url = newspaper_base_url + "category/শিল্প-সাহিত্য/11?page=" + str(index)
        elif j == 8: