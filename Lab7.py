def Programma():

or = open("ZADANIEXML.xml", 'r', encoding="utf-8")

ow = open("ZADANIEYAML.yaml", 'w', encoding="utf-8")

listXml = or.readlines()

countTab = 0;

for text in listXml:

ctext = text

while len(ctext) != 0:

if ctext[0] == ' ':

ctext = ctext[1:]

elif ctext[0] == '\n' or ctext[0] == '\t':

ctext = ctext[1:]

elif "</" in ctext[:2]:

countTab -= 1

l = ctext.find(">")

ctext = ctext[l+1:]

elif "<" in ctext[0]:

f = ctext.find("<")

l = ctext.find(">")

ow.write( countTab * ' ' + ctext[f+1:l] + ":" + '\n')

ctext = ctext[l+1:]

countTab += 1

else:

if "<" in ctext:

f = ctext.find("<")

if ":" in ctext[:f] or ctext[:f].isdigit():

ow.write( countTab * ' ' + "'" + ctext[:f] + "'" + '\n')

ctext = ctext[f:]

else:

ow.write( countTab * ' ' + ctext[:f] + '\n')

ctext = ctext[f:]

else:

if ":" in ctext or ctext.isdigit():

ow.write( countTab * ' ' + "'" + ctext + "'")

ctext = ctext[len(ctext):]

else:

ow.write( countTab * ' ' + ctext)

ctext = ctext[len(ctext):]

or.close()

ow.close()

def ParsingerWithRe():

import xmlplain

with open("ZADANIEXML.xml", "r", encoding="utf8") as inf:

root = xmlplain.xml_to_obj(inf, strip_space=True, fold_dict=True)

with open("ZADANIEYAML.yaml", "w", encoding="utf8") as outf:

xmlplain.obj_to_yaml(root, outf)

import time

print("Hello")

time1 = time.time()

for i in range(10):

Parsinge()

time1 = time.time() – time

time2 = time.time()

for i in range(10):

ParsingerWithRe()

time2 = time.time() - time2

print("Время нашего кода: " + str(time1) + '\n' + "Время готовой библиотеки: " + str(time2) + '\n' + "Наш код работает быстрее" if time2 > time1 else "Готовая библиотека быстрее")Ы