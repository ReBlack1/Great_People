# -*- coding: utf-8 -*-

import requests
from lxml import etree

def _Search_Ach_Palate_Boss(url):
    ACH_BOSS = etree.XPath("//div[@class = 'workes ruk'][1]/div[@class = 'desc']/a/@href")
    req = requests.get(url)
    html = etree.HTML(req.text)
    if str(req) == "<Response [200]>":
        return "http://www.ach.gov.ru" + ACH_BOSS(html)[0]
    else:
        return req

url_BOSS_AVATAR = "http://www.ach.gov.ru/images/lead1.png"
url_BOSS = _Search_Ach_Palate_Boss("http://www.ach.gov.ru/structure/")
print(url_BOSS)