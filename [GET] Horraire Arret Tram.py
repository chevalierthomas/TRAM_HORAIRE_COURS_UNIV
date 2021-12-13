# -*- coding: utf-8 -*-
"""
GET Horraire
"""
import requests
import json

nom_arrets = ["Bourgonnieres","Faculte","Ecoles centrale audencia","Hotel Dieu"];
arret_codetan = ["ECSU2","FACU2","BOGE2","HODI2"];

for i in range(len(nom_arrets)):
    url = "http://open.tan.fr/ewp/horairesarret.json/"+arret_codetan[i]+"/2/2"
    response = requests.get(url)
    data = response.json()
    data = data["horaires"]
    print("Horraire : ", nom_arrets[i])
    print(data)

    







