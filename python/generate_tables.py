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

def generate_table(txt_commands="vajrasana 120, shashankasana 180, adho_mukha_svanasana 60, uttanasana 120, baddha_konasana 60, upavishta_konasana 120, janu_sirsasana 60x2, paschimottanasana 240, shavasana 60, halasana 30, sarvangasana 60, utthita_sarvangasana 60x2, karnapidasana 30, halasana 30, shavasana 30, supta_baddha_konasana 300, shavasana 300", 
                   orig_adoc='/home/maurizio/GitBook/Library/maoz75/gli-appunti/14_yoga.adoc'):
    f=open(orig_adoc)
    orig_adoc = f.read()
    f.close()
    listed_table = txt_commands.split(', ')
    adoc_table = """.Tabella
    [header=yes, cols="^1,2,1"]
    |===
    | Posizione | Descrizione | Secondi
    """
    images=[]
    secs=[]
    descs=[]
    for elem in listed_table:
        image, sec = elem.split(' ')
        desc = find_description(orig_adoc,image.replace('_', ' '))
        pos_x = sec.find('x') # -1 not found
        times = 0 
        if pos_x > -1:
            times = int(sec[pos_x+1:])
            sec = sec[0:pos_x]
        images.append(image)
        descs.append(desc)
        secs.append(int(sec))
        adoc_table += "| image:figures/asana_yoga/{}.svg[role=right, pdfwidth=5cm] | {} | {} \n".format(image, desc, sec)
        for i in range(times-1):
            adoc_table += "| image:figures/asana_yoga/{}.svg[role=right, pdfwidth=5cm] | altro lato | {} \n".format(image, sec)
            images.append(image)
            descs.append('Cambia Lato')
            secs.append(int(sec))
    adoc_table += "|===\n"
    return images, descs, secs
    

def generate_srt_text(images, descs, secs, transition=1):
    """
    A numeric counter identifying each sequential subtitle
    The time  (00:00:00,000) that the subtitle should appear on the screen, followed by --> and the time it should disappear
    Subtitle text itself on one or more lines
    A blank line containing no text, indicating the end of this subtitle[9]
    """
    srt_text = ""
    act_time = transition
    for i in range (len(images)):        
        srt_text+="{:02d}\n00:{:02d}:{:02d},000-->00:{:02d}:{:02d},000\n{}: {}\n\n".format(
            i+1, 
            int(act_time/60), act_time%60, 
            int((act_time+secs[i])/60), (act_time+secs[i])%60, 
            images[i], descs[i])
        act_time+=secs[i]
    return srt_text

    
images, descs, secs = generate_table()
print(images, descs, secs )
print generate_srt_text(images, descs, secs)


        


