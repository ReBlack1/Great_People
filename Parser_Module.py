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

def _takeNextText(url, xpath, KEY_WORD, NAME_TAG, Flag = False):
    XPATH_A = _parser(url, xpath)
    RET_LIST = []
    for l in XPATH_A:
         if Flag == True and l.tag != NAME_TAG:
            Flag = False
         if l.text == KEY_WORD:
             Flag = True
         if Flag == True and l.tag == NAME_TAG:
             RET_LIST.append(l)
    return(RET_LIST)