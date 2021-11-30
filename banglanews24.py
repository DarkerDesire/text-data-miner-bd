
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
            url = newspaper_base_url + "category/লাইফস্টাইল/12?page=" + str(index)
        elif j == 9:
            url = newspaper_base_url + "/category/পর্যটন/13?page=" + str(index)
        elif j == 10:
            url = newspaper_base_url + "/category/চট্টগ্রাম-প্রতিদিন/14?page=" + str(index)
        elif j == 11:
            url = newspaper_base_url + "category/আইন-আদালত/18?page=" + str(index)
        elif j == 12:
            url = newspaper_base_url + "category/ইচ্ছেঘুড়ি/8?page=" + str(index)
        elif j == 13:
            url = newspaper_base_url + "category/প্রবাস/17?page=" + str(index)
        elif j == 14:
            url = newspaper_base_url + "category/স্বাস্থ্য/19?page=" + str(index)
        elif j == 15:
            url = newspaper_base_url + "category/শিক্ষা/20?page=" + str(index)
        elif j == 16:
            url = newspaper_base_url + "category/ইসলাম/15?page=" + str(index)
        elif j == 18:
            url = newspaper_base_url + "category/মুক্তমত/16?page=" + str(index)
        elif j == 19:
            url = newspaper_base_url + "category/জলবায়ু-পরিবেশ/21?page=" + str(index)