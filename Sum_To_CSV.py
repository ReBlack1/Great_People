# -*- coding: utf-8 -*-
import csv
import Gos_Dum
import Goverment
import MVD
import Parser_Module
import requests
from lxml import etree

def _makeNewBD():
    _csvWriter([["Structure", "Second_Name", "First_Name", "Third_Name", "Birthday", "Birthmonth", "Birthyear", "Photo", "ID", "KEY"]])

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


