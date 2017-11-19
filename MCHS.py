# -*- coding: utf-8 -*-
import Parser_Module
import requests
from lxml import etree

#Возвращает список URL
def _MCHSGetPerson():
    RET_LIST = []
    url = "http://www.mchs.gov.ru/ministry/management"
    xpath = './/div[@class="rukovodstvo"]/div//td/a[1]/@href'
    for i in Parser_Module._parser(url, xpath):
        RET_LIST.append("http://www.mchs.gov.ru" + i)
    return RET_LIST

#Возвращает строку с ФИО
def _MCHSPersonFIO(URL):
    xpath = './/article [@class="content clearfix"]/h1/text()'
    return Parser_Module._parser(URL, xpath)[0]

#Вернет str год рождения
def _MCHSPersonAge(URL):
    xpath = './/article [@class="content clearfix"]//p/text()'
    if len(Parser_Module._parser(URL, xpath)) > 3:
        for i in range(3):
            FLAG = False
            for j in Parser_Module._parser(URL, xpath)[i].replace(',', " ").split():
                if j == "Родился" or j == "родился" or j == "рождения":
                    FLAG = True
                if FLAG:
                    try:
                        int(j)
                        if int(j) > 1900:
                            return j
                    except:
                        pass
    return "not found"

#Возвращает url картинки
def _MCHSPersonImage(URL):
    xpath = './/article [@class="content clearfix"]/div/img/@src'
    try:
        return "http://www.mchs.gov.ru" + Parser_Module._parser(URL, xpath)[0]
    except:
        return "not found"

#Возвращает список с биографией
def _MCHSPersonBiography(URL):
    xpath = './/article [@class="content clearfix"]//p/text()'
    return Parser_Module._parser(URL, xpath)

print(_MCHSPersonImage("http://www.mchs.gov.ru/ministry/management/item/33195090/"))