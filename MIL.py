# -*- coding: utf-8 -*-
import Parser_Module
import requests
from lxml import etree

def _getMILPerson():
    RET_LIST = []
    url = "https://structure.mil.ru/management.htm"
    xpath = './/div[@class="leaderinfo"]/div/div/a[1]/@href'
    print(Parser_Module._parser(url, xpath))

_getMILPerson()
