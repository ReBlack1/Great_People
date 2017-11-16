# -*- coding: utf-8 -*-

import requests
from lxml import etree

def _parser(url, xpath):
    XPATH = etree.XPath(xpath)
    req = requests.get(url)
    html = etree.HTML(req.text)
    if str(req) == "<Response [200]>":
        return XPATH(html)
    else:
        return req