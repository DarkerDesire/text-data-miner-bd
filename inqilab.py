import os
import json
import time
from datetime import date, timedelta
from bs4 import BeautifulSoup
import requests


def month_converter(month):
    if m