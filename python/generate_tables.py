# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 23:36:46 2016

@author: maurizio
"""

def find_description(body,title):
    pos = body.find(title)
    if pos >-1:
        esec = '_Esecuzione_: '
        start = body.find(esec,pos) + len(esec)
        end = body.find(' +', start)
        #print pos, start, end, body[start:end]
        return body[start:end]
    else:
        return "ciccia"
    

f=open('/home/maurizio/GitBook/Library/maoz75/gli-appunti/14_yoga.adoc')
s = f.read()
f.close()

elenco = "vajrasana 120, shashankasana 180, adho_mukha_svanasana 60, uttanasana 120, baddha_konasana 60, upavishta_konasana 120, janu_sirsasana 60x2, paschimottanasana 240, shavasana 60, halasana 30, sarvangasana 60, utthita_sarvangasana 60x2, karnapidasana 30, halasana 30, shavasana 30, supta_baddha_konasana 300, shavasana 300"
lista = elenco.split(', ')


tabella = """.Tabella
[header=yes, cols="^1,2,1"]
|===
| Posizione | Descrizione | Secondi
"""
for elem in lista:
    image, secs = elem.split(' ')
    pos_x = secs.find('x') # -1 not found
    desc = find_description(s,image.replace('_', ' '))
    if pos_x > -1:
        times = int(secs[pos_x+1:])
        new_secs = secs[0:pos_x]
        tabella += "| image:figures/asana_yoga/{}.svg[role=right, pdfwidth=5cm] | {} | {} \n".format(image, desc, new_secs)
        for i in range(times-1):
            tabella += "| image:figures/asana_yoga/{}.svg[role=right, pdfwidth=5cm] | altro lato | {} \n".format(image, new_secs)
    else:
        tabella += "| image:figures/asana_yoga/{}.svg[role=right, pdfwidth=5cm] | {} | {} \n".format(image, desc, secs)
tabella += "|===\n"
print tabella

