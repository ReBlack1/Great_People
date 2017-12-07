# -*- coding: utf-8 -*-
import Parser_Module
import requests
from lxml import etree
import csv
import Gos_Dum
import Goverment
import MVD
import MCHS
import math

def _educationAnalys(BIOGRAPHY_LIST):
    RET_LIST = []
    for i in BIOGRAPHY_LIST:
        s = i.split(".")
        for j in s:
            j = j.lower()
            if math.fabs( j.find("универ") *  j.find("институт") * j.find("колледж")*j.find("академ")*j.find("училище")) != 1:
                RET_LIST.append(j)
    return RET_LIST

def _getEducation(STRUCTURE, URL):
    if STRUCTURE == "GD":
        return Gos_Dum._GosDumPersonEducation(URL)
    if STRUCTURE == "MCHS":
        return _educationAnalys(MCHS._MCHSPersonBiography(URL))
    if STRUCTURE == "MVD":
        return _educationAnalys(MVD._MVDPersonBiography(URL))
    if STRUCTURE == "Goverment":
        return _educationAnalys(Goverment._GovermentPersonBiography(URL))


def _scvReaderQ(Q_LINE):
    RET_LIST = []
    q = 0
    with open("BD.csv", "r", newline='') as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            if q == 0:
                q += 1
                continue
            RET_LIST.append([line[0],line[8]])
            q += 1
            if q > Q_LINE:
                return RET_LIST
def _scvReader():
    RET_LIST = []
    Q_EDC = [0,0,0,0,0]
    FLAG = True
    with open("BD.csv", "r", newline='') as csv_file:
        reader = csv.reader(csv_file)
        sum = 0
        for line in reader:

            for j in line[8].replace(",", "|").split("|"):
                j = j.lower()
                if math.fabs(j.find("")) != 1:
                    sum += 1
                    print(line[1])
                    print(line[0])
                    print(line[8])
    print(sum)
    return RET_LIST


##A = _scvReader()
##Bio = []
##for i in A:
##    Bio.append(_getEducation(i[0], i[1]))
##print(Bio)
##A = ['В 1993 г. окончил юридический факультет Московского Государственного Университета им.М.В.Ломоносова по специальности «правоведение».', '1984-1985 гг. - лаборант в Научно-исследовательском институте «Экос».', '1985-1987 гг. - служба в рядах Советской Армии.', 'В 1993 г. - атташе Правового департамента Министерства иностранных дел Российской Федерации.', '1993-1995 гг. - старший юрисконсульт АОЗТ «АЛМ Консалтинг», с 1995 г. - директор адвокатского бюро «АЛМ».', 'В 1997 г. - начальник Департамента государственного реестра федеральной собственности Государственного комитета России по управлению государственным имуществом.', 'В 1998 г. - заместитель Министра государственного имущества Российской Федерации.', '1998-2000 гг. - Председатель Российского фонда федерального имущества.', '2000-2003 гг. - Руководитель Аппарата Правительства Российской Федерации - Министр Российской Федерации.', 'В 2003 г. - помощник Президента Российской Федерации.', '2003-2004 гг. - заместитель Руководителя Администрации Президента Российской Федерации.', 'В 2004 г.- помощник Президента Российской Федерации.', 'С 2005 г. является также российским «шерпой» в «Группе восьми».', '\xa0С 2008 г. - Первый заместитель Председателя Правительства Российской Федерации.', 'Женат. Четверо детей: два сына и две дочери.']
##print (_educationAnalys(A))
_scvReader()