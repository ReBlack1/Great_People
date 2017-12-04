# -*- coding: utf-8 -*-
import Parser_Module
import requests
from lxml import etree

#Возвращает список URL
def _getMILPerson():
    url = "https://structure.mil.ru/management.htm"
    xpath = './/div[@class="leaderinfo"]/div/div/a[1]/@href'
    ex_xpath = './/div[@class="sp-wrap"]//a[@class="index"]/@href'
    BOSS = Parser_Module._parser(url, xpath)
    RET_LIST = Parser_Module._parser(url, ex_xpath)
    for i in BOSS:
        RET_LIST.append("structure.mil.ru/" + i)
    return RET_LIST

print(_getMILPerson())
