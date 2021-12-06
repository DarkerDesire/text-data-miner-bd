
import os
import json
import time
from datetime import date, timedelta
from bs4 import BeautifulSoup
import requests

# from io import open

newspaper_base_url = 'https://www.bd-pratidin.com/'

output_result = []
data = []
exceptions = 0

for i in range(100):
    index = i * 12

    for j in range(28):
        if j == 0: