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

#Возращает список с датой рождения
def _GovermentPersonAge(URL_PERSON):
    url = URL_PERSON + "biography/"
    xpath = ".//div[@class='reader']//div[@class='reader_article ']/div[@class='reader_article_body']/p"
    return Parser_Module._parser(url, xpath)[1].text.split()[1:4]

#Возвращает биографию депутата в массиве
def _GovermentPersonBiography(URL_PERSON):
    RET_LIST = []
    url = URL_PERSON + "biography/"
    xpath = ".//div[@class='reader']//div[@class='reader_article ']/div[@class='reader_article_body']/p"
    for i in Parser_Module._parser(url, xpath)[2:]:
        RET_LIST.append(i.text)
    return RET_LIST

def _GovermentPersonFIO(URL_PERSON):
    xpath = './/p[@class="vcard_name"]'
    return Parser_Module._parser(URL_PERSON, xpath)[0].text

def _GovermentPersonImage(URL_PERSON):
    xpath = './/div[@class="vcard_photo"]/img/@src'
    return Parser_Module._parser(URL_PERSON, xpath)[0]

