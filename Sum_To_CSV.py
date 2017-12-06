# -*- coding: utf-8 -*-
import csv
import Gos_Dum
import Goverment
import MVD
import MCHS
import Parser_Module
import requests
import Education_Analys
from lxml import etree

def _UpgradeAll():
    _makeNewBD()
    print("I made new BD")
    _UpgradeGosDum()
    print("I upgrade GD")
    _UpgradeGoverment()
    print("I upgrade Goverment")
    _UpgradeMVD()
    print("I upgrade MVD")
    _UpgradeMCHS()
    print("I upgrade MCHS")


def _makeNewBD():
    _csvWriter([["Structure", "Second_Name", "First_Name", "Third_Name", "Birthday", "Birthmonth", "Birthyear", "Photo", "Education", "ID/URL", "KEY"]])

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
#Обновляем БД в госдуме
def _UpgradeGosDum():
    ALFABET = ["А","Б","В","Г","Д","Е","Ж","З","И","К","Л","М","Н","О","П","Р","С","Т","У","Ф","Х","Ш","Щ","Э","Ю","Я"]
    for i in ALFABET:
        LIST_DEPUTY = Gos_Dum._GosDumSearch(i)
        for j in LIST_DEPUTY:
            SUM_LIST = []
            ID = j[1]
            FIO = j[0].split()
            AGE = Gos_Dum._GosDumPersonAge(ID)
            PHOTO = Gos_Dum._GosDumPersonImg(ID)
            Edc = ""
            for f in Education_Analys._getEducation("GD", ID):
                for k in f.split(","):
                    Edc = Edc + k + "|"
            KEY = Gos_Dum._GosDumPersonGetKey(j[0])
            SUM_LIST.append(["GD", FIO[0], FIO[1], FIO[2], AGE[0], AGE[1], AGE[2], PHOTO, Edc, ID, KEY])

            _csvAppend(SUM_LIST)

def _UpgradeGoverment():
    URL_LIST = Goverment._GovermentExBossPersonURL()
    URL_LIST.append(Goverment._GovermentBossPersonURL())
    SUM_LIST = []
    for i in URL_LIST:
        FIO = Goverment._GovermentPersonFIO(i).split()
        AGE = Goverment._GovermentPersonAge(i)
        IMG = Goverment._GovermentPersonImage(i)
        Edc = ""
        for j in Education_Analys._getEducation("Goverment", i):
            for k in j.split(","):
                Edc = Edc + k + "|"
        SUM_LIST.append(["Goverment", FIO[2], FIO[1], FIO[1], AGE[0], AGE[1], AGE[2], IMG, Edc, i])
    _csvAppend(SUM_LIST)

def _UpgradeMVD():
    ID_LIST = MVD._MVDGetPerson()
    SUM_LIST = []
    for i in ID_LIST:
        FIO = MVD._MVDPersonFIO(i).split()
        AGE = MVD._MVDPersonAge(i)
        IMG = MVD._MVDPersonImage(i)
        Edc = ""
        for j in Education_Analys._getEducation("MVD", i):
            for k in j.split(","):
                Edc = Edc + k + "|"
        SUM_LIST.append(["MVD", FIO[0], FIO[1], FIO[2], "None", "None", AGE, IMG, Edc, i])
    _csvAppend(SUM_LIST)

def _UpgradeMCHS():
    URL_LIST = MCHS._MCHSGetPerson()
    SUM_LIST = []
    z = ""
    for i in URL_LIST:

        FIO = MCHS._MCHSPersonFIO(i).split()
        try:
            AGE = MCHS._MCHSPersonAge(i)
        except:
            AGE = "not found"
        try:
            IMG = MCHS._MCHSPersonImage(i)
        except:
            IMG = "not found"
        Edc = ""
        for j in Education_Analys._getEducation("MCHS", i):
            for k in j.split(","):
                Edc = Edc + k + "|"
        print(i)
        SUM_LIST.append(["MCHS", FIO[0], FIO[1], FIO[2], "None", "None", AGE, IMG, Edc, i])
    _csvAppend(SUM_LIST)

##_makeNewBD()
_UpgradeAll()