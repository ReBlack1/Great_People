# -*- coding: utf-8 -*-
import Parser_Module

#ВОзвращает список списков где в 0-ФИО депутатов, 1-Их ID
def _GosDumSearch():
    ALFABET = ["А", "Б", "В", "Г", "Д"]
    xpath = ".//a"
    RET_LIST = [[],[]]
    for i in ALFABET:
        url = "http://www.duma.gov.ru/about/personnel/property/deputies/?letter=" + i
        DEPUTY_LIST = Parser_Module._parser(url, xpath)
        for r in DEPUTY_LIST:
            if str(r.attrib)[:-10] == "{'href': '/structure/deputies/" and r.text != "Председатель ГД":
                RET_LIST[0].append(r.text)
                RET_LIST[1].append(str(r.attrib)[-10:-3])
    return(RET_LIST)
#_GosDumSearch()

def _GosDumPersonImg(ID):
    url = 'http://www.duma.gov.ru/structure/deputies/'+ str(ID) + "/"
    xpath_photo = ".//body/div[@id = 'wrap']/div [@id = 'main']/div [@id = 'left-col']/div [@class = 'deputat-info']//img/@src"
    PHOTO = "http://www.duma.gov.ru" + Parser_Module._parser(url, xpath_photo)[0]
    return(PHOTO)

def _GosDumPersonEducation(ID):
    url = 'http://www.duma.gov.ru/structure/deputies/'+ str(ID) + "/"
    xpath_education = ".//body/div[@id = 'wrap']/div [@id = 'main']/div [@id = 'left-col']/div [@class = 'deputat-info']/div [@class = 'deputat-info-right']/*"
    LIST = Parser_Module._takeNextText(url, xpath_education, "Образование", 'ul')
    RET_LIST = []
    for i in LIST[0].getchildren():
        RET_LIST.append(i.text)
    return RET_LIST

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

print(_GosDumPersonEducation(1756721))
##def _GosDumSpeechParser(ID):
    ##url_speech = 'http://cir.duma.gov.ru/duma/servlet/is4.wwwmain?FormName=ShowResult&QueryID=' +str('ID')+ '&Page=1&ShowMax=200'
    ##req_speech= requests.get(url_speech)
    ##html_speech = etree(req_speech.text)
    ##if str(req_speech) == "<Response [200]>":




