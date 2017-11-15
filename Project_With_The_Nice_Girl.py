# -*- coding: utf-8 -*-

import requests
from lxml import etree

def _GosDumSearch():
    ##ALFABET = ["А", "Б", "В", "Г", "Д", "Е", "Ж", "З", "И", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф", "Х", "Ш", "Щ", "Э", "Ю", "Я"]
    ALFABET = ["А", "Б", "В"]
    for i in ALFABET:
        _Parser("http://www.duma.gov.ru/about/personnel/property/deputies/?letter=" + i)

def _Parser(url):
    GOS_DUM = etree.XPath(".//a")
    req = requests.get(url)
    html = etree.HTML(req.text)
    if str(req) == "<Response [200]>":
        print('I am connect')
        for r in GOS_DUM(html):
            if str(r.attrib)[:30] == "{'href': '/structure/deputies/" and r.text != "Депутаты Государственной Думы" and r.text != "Председатель ГД" and r.text != "Депутаты ГД":
                print(r.text , end=" ID = ")
                print(str(r.attrib)[-10:-3])
##_GosDumSearch()

def _GosDumPersonParser(ID):
    url = 'http://www.duma.gov.ru/structure/deputies/'+ str(ID) + "/"
    req = requests.get(url)
    html = etree.HTML(req.text)
    PHOTO = etree.XPath(".//body/div[@id = 'wrap']/div [@id = 'main']/div [@id = 'left-col']/div [@class = 'deputat-info']//img")
    EDUCATION = etree.XPath(".//body/div[@id = 'wrap']/div [@id = 'main']/div [@id = 'left-col']/div [@class = 'deputat-info']/div [@class = 'deputat-info-right']/ul[@class = 'list-ul1'][3]/*")
    EDUCATION_MORE = etree.XPath(".//body/div[@id = 'wrap']/div [@id = 'main']/div [@id = 'left-col']/div [@class = 'deputat-info']/div [@class = 'deputat-info-right']/ul[@class = 'list-ul1'][4]/*")
    if str(req) == "<Response [200]>":
        for r in PHOTO(html):
            print("http://www.duma.gov.ru" + str(r.attrib).split(",")[3][9:-2])
        for k in EDUCATION_MORE(html):
            print(k.text)


def _GosDumSpeechParser(ID):
    url_speech = 'http://cir.duma.gov.ru/duma/servlet/is4.wwwmain?FormName=ShowResult&QueryID=' +str('ID')+ '&Page=1&ShowMax=200'
    req_speech= requests.get(url_speech)
    html_speech = etree(req_speech.text)
    if str(req_speech) == "<Response [200]>":






