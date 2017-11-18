# -*- coding: utf-8 -*-
import csv
import Gos_Dum
import Goverment
import MVD
import Parser_Module
import requests
from lxml import etree

def _UpgradeAll():
    _makeNewBD()
    _UpgradeGosDum()
    _UpgradeGoverment()
    _UpgradeMVD()

def _makeNewBD():
    _csvWriter([["Structure", "Second_Name", "First_Name", "Third_Name", "Birthday", "Birthmonth", "Birthyear", "Photo", "ID/URL", "KEY"]])

#Закидываешь туда массив из массивов и он делает из этого файлик с БД
def _csvWriter(data):
    with open("BD.csv", "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)

    print("I am save")

#Закидываешь туда массив из массивов он в файлик добаляет новые строки
def _csvAppend(data):
    with open("BD.csv", "a", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)

    print("I am append")

def _UpgradeGosDum():
    ALFABET = ["А","Б","В","Г","Д","Е","Ж","З","И","К","Л","М","Н","О","П","Р","С","Т","У","Ф","Х","Ш","Щ","Э","Ю","Я"]
    for i in ALFABET:
        LIST_DEPUTY = Gos_Dum._GosDumSearch(i)
        LIST_KEY_DEPUTY = []
        LIST_DEPUTY_AGE = []
        LIST_DEPUTY_PHOTO = []
        SUM_LIST = []
        for j in LIST_DEPUTY[0]:
            LIST_KEY_DEPUTY.append(Gos_Dum._GosDumPersonGetKey(j))
        for k in LIST_DEPUTY[1]:
            LIST_DEPUTY_AGE.append(Gos_Dum._GosDumPersonAge(k))
        for q in LIST_DEPUTY[1]:
            LIST_DEPUTY_PHOTO.append(Gos_Dum._GosDumPersonImg(q))
        for z in range(len(LIST_DEPUTY[0])):
            SUM_LIST.append(["GD", LIST_DEPUTY[0][z].split()[0], LIST_DEPUTY[0][z].split()[1], LIST_DEPUTY[0][z].split()[2], LIST_DEPUTY_AGE[z][0],LIST_DEPUTY_AGE[z][1],
            LIST_DEPUTY_AGE[z][2], LIST_DEPUTY_PHOTO[z], LIST_DEPUTY[1][z], LIST_KEY_DEPUTY[z]])
        _csvAppend(SUM_LIST)

def _UpgradeGoverment():
    URL_LIST = Goverment._GovermentExBossPersonURL()
    URL_LIST.append(Goverment._GovermentBossPersonURL())
    SUM_LIST = []
    for i in URL_LIST:
        FIO = Goverment._GovermentPersonFIO(i).split()
        AGE = Goverment._GovermentPersonAge(i)
        IMG = Goverment._GovermentPersonImage(i)
        SUM_LIST.append(["Goverment", FIO[2], FIO[1], FIO[1], AGE[0], AGE[1], AGE[2], IMG, i])
    _csvAppend(SUM_LIST)

def _UpgradeMVD():
    ID_LIST = MVD._MVDGetPerson()
    SUM_LIST = []
    for i in ID_LIST:
        FIO = MVD._MVDPersonFIO(i).split()
        AGE = MVD._MVDPersonAge(i)
        IMG = MVD._MVDPersonImage(i)
        SUM_LIST.append(["MVD", FIO[0], FIO[1], FIO[2], "None", "None", AGE, IMG, i])
    _csvAppend(SUM_LIST)
