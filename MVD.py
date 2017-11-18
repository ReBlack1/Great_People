# -*- coding: utf-8 -*-
import Parser_Module
import requests
from lxml import etree

#Возвращает массив из ID МВД
def _MVDGetPerson():
    RET_LIST = []
    url = "https://xn--b1aew.xn--p1ai/mvd/structure1"
    xpath = './/ul[@class="ministers_list new_ministers_list"]/li/a/@href'
    for i in Parser_Module._parser(url, xpath):
        RET_LIST.append(i[-6:])
    return RET_LIST

#Возвращает массив с биографией члена МВД
def _MVDPersonBiography(ID):
    RET_LIST = []
    url = "https://мвд.рф/mvd/Rukovodstvo/item/" + str(ID) + "/"
    xpath = './/div[@class="ln-content-holder"]/div[@class="news_block block_size14"]/p'
    for i in Parser_Module._parser(url,xpath):
        if i.text != None:
            RET_LIST.append(i.text)
    return RET_LIST

#Вернет только год раждения
def _MVDPersonAge(ID):
    url = "https://мвд.рф/mvd/Rukovodstvo/item/" + str(ID) + "/"
    xpath = './/div[@class="ln-content-holder"]/div[@class="news_block block_size14"]/p'
    BLOCK_AGE = Parser_Module._parser(url,xpath)[0].text
    AGE = BLOCK_AGE.split("года")[0]
    AGE = AGE.split("г")[0]
    AGE = AGE.split()[-1]
    return AGE

#Вернет ссылку на фотку члена МВД
def _MVDPersonImage(ID):
    url = "https://мвд.рф/mvd/Rukovodstvo/item/" + str(ID) + "/"
    xpath = './/div [@class="sd-image"]/img/@src'
    return Parser_Module._parser(url, xpath)[0]
