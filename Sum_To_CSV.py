# -*- coding: utf-8 -*-
import csv
import Gos_Dum
import Goverment
import MVD
import Parser_Module
import requests
from lxml import etree

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
    for i in ALFABET[:4]:
        LIST_DEPUTY = Gos_Dum._GosDumSearch(i)



_UpgradeGosDum()
