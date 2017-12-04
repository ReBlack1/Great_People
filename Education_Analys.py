# -*- coding: utf-8 -*-
import Parser_Module
import requests
from lxml import etree
import csv
import Gos_Dum

def _educationAnalys(BIOGRAPHY_LIST):
    RET_LIST = []
    for i in BIOGRAPHY_LIST:
        s = i.replace(",", " ").split()
        for j in s:
            if j.lower()[:6] == "универ" or j.lower()[:8] == "институт" or j.lower()[:7] == "колледж" or j.lower()[:8] == "академия" or j.lower()[:7] == "училище":
                RET_LIST.append(i)
    return RET_LIST

def _getBiograhpy(STRUCTURE, URL):
    if STRUCTURE == "GD":
        return Gos_Dum._GosDumPersonEducation(URL)

def _scvReader(Q_LINE):
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
for i in range(300):
    print(_educationAnalys( _getBiograhpy( _scvReader(400)[i][0], _scvReader(400)[i][1])))
##    print( _getBiograhpy( _scvReader(10)[i][0], _scvReader(10)[i][1]))