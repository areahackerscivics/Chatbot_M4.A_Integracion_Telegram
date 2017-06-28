#!/usr/bin/python
# -*- coding: utf-8 -*-

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Librerias
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
import requests
import json

from variables import *


##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Variables
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
try:
    apiAccess = os.environ['APIAI_ACCESS_TOKEN']
    apiDeveloperAccess = os.environ['DEVELOPER_ACCESS_TOKEN']

except:
    print "Error al cargar tokens de api.ai"

baseURL = "https://api.api.ai/v1/"
v = 20170605 # fecha en formato AAAAMMDD
APIAI_LANG = "es"

headers = {
    'Authorization': 'Bearer '+apiAccess,
    "Content-Type":"application/json; charset=utf-8"
    }


##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Funciónes
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def sendQuery(texto, chat_id, idioma, nombreUsuario):
    contexto = [{
        "name": "usuario",
        "parameters": { "idioma": idioma, "nombre": nombreUsuario },
        "lifespan": 1
        }]
    payload = {
        "query": texto,
        "v": v,
        "sessionId": chat_id,
        "contexts": contexto,
        "lang": APIAI_LANG
        }

    url = baseURL+"query"

    r = requests.post(url, data=json.dumps(payload), headers=headers)

    return r
