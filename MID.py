# -*- coding: utf-8 -*-
import Parser_Module
import requests
from lxml import etree

# Возвращает массив из босса и заместителей по МИД
def _getMIDPerson():
    url = "http://www.mid.ru/ru/about/structure"
    xpath_boss = './/ul[@class="layouts level-1 anons-list-without-dates"]/li[1]/h2/a/@href'
    xpath_ex_boss = './/ul[@class="layouts level-1 anons-list-without-dates"]/li[2]/h2/a/@href'
    ex_url = Parser_Module._parser(url, xpath_ex_boss)[0]
    ex_xpath = './/ul [@class="three-cols-list structure-list"]/li/a/@href'
    RET_LIST = Parser_Module._parser(ex_url, ex_xpath)
    RET_LIST.append(Parser_Module._parser(url, xpath_boss)[0])
    return RET_LIST

#Возвращает ФИО
def _getMIDFIO(URL):
    xpath = './/div[@class="text text-part"]/h1/text()'
    return Parser_Module._parser(URL, xpath)[0]

#Возвращает ссылку на фото
def _getMIDImage(URL):
    xpath = './/div[@class="journal-content-article"]//img/@src'
    return "http://www.mid.ru" + Parser_Module._parser(URL, xpath)[0]

#Возвращает массив с биографией
def _getMIDBiography(URL):
    xpath = './/div[@class="journal-content-article"]/div/p/text()'
    return Parser_Module._parser(URL, xpath)

#Возвращает str год рождения
def _getMIDAge(URL):
    xpath = './/div[@class="journal-content-article"]/div/p/text()'
    Biography = Parser_Module._parser(URL, xpath)
    for i in Biography:
        Flag = False
        for j in i.replace(",", " ").split():
            if j == "Родился":
                Flag = True
            if Flag:
                try:
                    if int(j) > 1900:
                        return j
                except:
                    pass
    return "not found"
