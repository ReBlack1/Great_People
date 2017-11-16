# -*- coding: utf-8 -*-
import requests
from lxml import etree

API_KEY = "a630ac18d0b1ff11588ec52d13efe95b22dff73d"
API_KEY_APP = "app5d5b7866eb2ba3f6ddb0bf8faf304ed5e312b414"

url = "http://api.duma.gov.ru/api/" + API_KEY + "/deputies.xml?app_token=" + API_KEY_APP
req = requests.get(url)
html = etree.HTML(req.text)

print(req.text)