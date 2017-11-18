# -*- coding: utf-8 -*-
import Parser_Module
import requests
from lxml import etree

#Возвращает список ссылок на Заместителей главы правительства
def _GovermentExBossPersonURL():
    RET_LIST = []
    url = "http://government.ru/gov/persons/#vice-premiers"
    xpath = ".//li[@id='vice-premiers']/ul/li/a[@class='person_slide']/@href"
    for i in Parser_Module._parser(url, xpath):
        RET_LIST.append("http://government.ru" + str(i))
    return RET_LIST

#Возвращает ссылку на Главу правительства
def _GovermentBossPersonURL():
    url = "http://government.ru/gov/persons/#vice-premiers"
    xpath = ".//li[@class='person person__large']/a[@class='person_slide']/@href"
    return "http://government.ru" + str(Parser_Module._parser(url, xpath)[0])


print(_GovermentExBossPersonURL())