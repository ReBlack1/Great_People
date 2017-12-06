# -*- coding: utf-8 -*-
import Parser_Module
import requests
from lxml import etree
import csv
import Gos_Dum
import Goverment
import MVD
import MCHS

def _educationAnalys(BIOGRAPHY_LIST):
    RET_LIST = []
    for i in BIOGRAPHY_LIST:
        s = i.replace(",", " ").split()
        for j in s:
            if j.lower()[:6] == "универ" or j.lower()[:8] == "институт" or j.lower()[:7] == "колледж" or j.lower()[:8] == "академия" or j.lower()[:7] == "училище":
                RET_LIST.append(i)
    return RET_LIST

def _getEducation(STRUCTURE, URL):
    if STRUCTURE == "GD":
        return Gos_Dum._GosDumPersonEducation(URL)
    if STRUCTURE == "MCHS":
        return _educationAnalys(MCHS._MCHSPersonBiography(URL))
    if STRUCTURE == "MVD":
        return _educationAnalys(MVD._MVDPersonBiography(URL))
    if STRUCTURE == "Goverment":
        return "no found"


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
    FLAG = True
    with open("BD.csv", "r", newline='') as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            if FLAG:
                FLAG = False
                continue
            RET_LIST.append([line[0],line[8]])
    return RET_LIST

##A = _scvReader()
##Bio = []
##for i in A:
##    Bio.append(_getEducation(i[0], i[1]))
##print(Bio)