# -*- coding: utf-8 -*-
import Parser_Module
import requests
from lxml import etree
API_KEY = "c3fee5876f89bd7d9cf05d87a0b21f2de7fa42ea"
API_KEY_APP = "appf038c62e1646f599a6700e2df004d7ae4edcb6dd"

#Просит первую букву для фамилий списка депутатов
#ВОзвращает список списков где в 0-ФИО депутатов, 1-Их ID
def _GosDumSearch(LETTER):
    xpath = ".//a"
    RET_LIST = []
    url = "http://www.duma.gov.ru/about/personnel/property/deputies/?letter=" + LETTER
    DEPUTY_LIST = Parser_Module._parser(url, xpath)
    for r in DEPUTY_LIST:
        if str(r.attrib)[:-10] == "{'href': '/structure/deputies/" and r.text != "Председатель ГД":
            RET_LIST.append([r.text, str(r.attrib)[-10:-3]])
    return(RET_LIST)

# Возвращает ссылку на фото депутата
def _GosDumPersonImg(ID):
    url = 'http://www.duma.gov.ru/structure/deputies/'+ str(ID) + "/"
    xpath_photo = ".//body/div[@id = 'wrap']/div [@id = 'main']/div [@id = 'left-col']/div [@class = 'deputat-info']//img/@src"
    PHOTO = "http://www.duma.gov.ru" + Parser_Module._parser(url, xpath_photo)[0]
    return(PHOTO)

# Возвращает массив с образовательными учереждениями, которые окончил депутат
def _GosDumPersonEducation(ID):
    url = 'http://www.duma.gov.ru/structure/deputies/'+ str(ID) + "/"
    xpath_education = ".//body/div[@id = 'wrap']/div [@id = 'main']/div [@id = 'left-col']/div [@class = 'deputat-info']/div [@class = 'deputat-info-right']/*"
    LIST = Parser_Module._takeNextText(url, xpath_education, "Образование", 'ul')
    RET_LIST = []
    try:
        for i in LIST[0].getchildren():
            RET_LIST.append(i.text)
    except:
        return ["no found"]
    return RET_LIST
#Возвращает список с темами выступлений
def _GosDumPersonSpeechName(KEY_DEPUTY):
    url = "http://api.duma.gov.ru/api/" + API_KEY + "/transcriptDeputy/" + str(KEY_DEPUTY) + ".xml?limit=20" + "&app_token=" + API_KEY_APP
    xpath_count = ".//body/result/totalcount"
    page_count = int(Parser_Module._parser(url, xpath_count)[0].text) // 20 + 1
    RET_LIST = []
    for i in range(1, page_count):
        url = "http://api.duma.gov.ru/api/" + API_KEY + "/transcriptDeputy/" + str(KEY_DEPUTY) + ".xml?limit=20&page=" + str(i) + "&app_token=" + API_KEY_APP
        xpath_speech = ".//name"
        for i in (Parser_Module._parser(url, xpath_speech)[1:]):
            RET_LIST.append(i.text)
    return RET_LIST

#Возвращает str с ключом депутата гос думы
def _GosDumPersonGetKey(FIO):
    FIRST_LETTER = FIO.split()[0]
    url = "http://api.duma.gov.ru/api/" + API_KEY + "/deputies.xml?begin=" + str(FIO) + "&current=1" + "&app_token=" + API_KEY_APP
    xpath_key = ".//body/result/deputy/id"
    RET_LIST = Parser_Module._parser(url, xpath_key)
    if len(RET_LIST) > 0:
        return RET_LIST[0].text
    else:
        return "Not found"

#Возвращает массив с тремя элементами 0- день 1- месяц буквами 2- год рождения
def _GosDumPersonAge(ID):
    url = 'http://www.duma.gov.ru/structure/deputies/'+ str(ID) + "/"
    xpath_age = ('.//p[@class="deputat-info-date"]')
    try:
        return Parser_Module._parser(url, xpath_age)[0].text.split()[2:-1]
    except:
        return ["no found","no found","no found"]

##    EDUCATION_MORE = etree.XPath(".//body/div[@id = 'wrap']/div [@id = 'main']/div [@id = 'left-col']/div [@class = 'deputat-info']/div [@class = 'deputat-info-right']/ul[@class = 'list-ul1']/*")
##    EDUCATION_ACHIEVEMENT =  etree.XPath(".//body/div[@id = 'wrap']/div [@id = 'main']/div [@id = 'left-col']/div [@class = 'deputat-info']/div [@class = 'deputat-info']/div [@class = 'deputat-info-right']/ul[@class = 'list-ul1']/*")
##    BIOGRAHY = etree.XPath(".//body/div[@id = 'wrap']/div [@id = 'main']/div [@id = 'left-col']/div [@class = 'deputat-info']/div [@class = 'deputat-info-right']/*")
##    FlagEducation = False
##    FlagEducationMore = False
##    FlagBiograhy = False
##    FlagEducationAchievement = False
##    if str(req) == "<Response [200]>":
##         for l in EDUCATION(html):
##             if l.text == 'РћР±СЂР°Р·РѕРІР°РЅРёРµ':
##                 FlagEducation = True
##             if FlagEducation == True and l.tag == 'p':
##                 print(l.text)
            # if l.text == 'РЈС‡РµРЅС‹Рµ СЃС‚РµРїРµРЅРё':
            #     FlagEducationMore == True
            # if FlagEducationMore == True:
            #     print(l.text)
            # FlagEducationMore = False
            # if l.text == 'РЈС‡РµРЅС‹Рµ Р·РІР°РЅРёСЏ':
            #     FlagEducationAchievement = True
            # if FlagEducationAchievement == True:
            #     print(l.text)
             #FlagEducationAchievement = False
        # for l in BIOGRAHY(html):
        #     if l.text == 'Р‘РёРѕРіСЂР°С„РёСЏ':
        #          FlagBiograhy = True
        #     if FlagBiograhy == True and l.tag == 'p':
        #          print(l.text)







