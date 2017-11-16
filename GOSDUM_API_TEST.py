# -*- coding: utf-8 -*-
import requests
from lxml import etree

API_KEY = "c3fee5876f89bd7d9cf05d87a0b21f2de7fa42ea"
API_KEY_APP = "appf038c62e1646f599a6700e2df004d7ae4edcb6dd"

url = "http://api.duma.gov.ru/api/" + API_KEY + "/deputies.xml?begin=А&app_token=" + API_KEY_APP
req = requests.get(url)
html = etree.HTML(req.text)

print(req.text)