
"""
GET Première heure de cours
"""

import requests

response = requests.get("https://edt-v2.univ-nantes.fr/events?start=2021-09-08&end=2021-12-30&timetables%5B0%5D=53366")
edt = response.json()
date = []
date_all = []
matiere = []
nom_matiere = []
#On check tout les items de l'api et on récupere la date et les heure ou les cours commence

for i in range(len(edt)):
    date_all.append([])
    
    date.append(edt[i]["start_at"][0:10])
    date.append(edt[i]["start_at"][11:16])
    date.append(edt[i]["categories"])
    date.append(edt[i]["modules_for_blocks"])
    date_all[i].extend(date)
    date.clear()    

kill_doublon = []

#On check tout les element de la liste et on conpare la date de tout les element i et i+1 si il sont identique cela signifie que i+1 n'est pas le premier cours de la journée
#On recupère tout les i+1 dans une liste
for i in range(len(date_all)-1):

    if (date_all[i][0] == date_all[i+1][0]):

        kill_doublon.append(i+1)

#on retire de la liste tout les i + 1
for i in range(len(kill_doublon)):
    uwu =(kill_doublon[i])

    del date_all[uwu][0:4]
    
date_all = list(filter(None, date_all))

date_final = []
heure_final = []

for i in range(len(date_all)-1):
    date_final.append(date_all[i][0])
    heure_final.append(date_all[i][1])
    matiere.append(date_all[i][2] + " : " +  date_all[i][3][10:(len(date_all[i][3]))])
    

print(date_final,heure_final,matiere,nom_matiere)

    


