# -*- coding: utf-8 -*-
import Parser_Module

xpath_search_boss = "//div[@class = 'workes ruk'][1]/div[@class = 'desc']/a/@href"
url_search_boss = "http://www.ach.gov.ru/structure/"
URL_BOSS_AVATAR = "http://www.ach.gov.ru/images/lead1.png"
URL_BOSS = "http://www.ach.gov.ru" + Parser_Module._parser(url_search_boss, xpath_search_boss)[0]

xpath_biography = "//div[@class = 'tab_content_imit']/*"

BIORGRAPHY = Parser_Module._takeNextText(URL_BOSS, xpath_biography, "", "p", True)

for i in BIORGRAPHY:
    print(i)