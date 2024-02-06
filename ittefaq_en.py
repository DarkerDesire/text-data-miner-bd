
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