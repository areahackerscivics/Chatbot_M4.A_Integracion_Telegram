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
    WebHook_URL = os.environ['WebHook_URL']
except:
    print "Error al cargar la URL del WebHook"


def buscarRespuestaWH(r):
    """La variable 'resultado' será pasado como diccionario con
    el esquema de respuesta de api.ai. Solo se llamara a la
    función cuando webhookUsed = 'true' """
    print 'Hola desde WH'

    res = requests.post(WebHook_URL, data=json.dumps(r))

    # print type(r) # <class 'requests.models.Response'>
    # r = r.json()
    # print type(r) # <type 'dict'>
    # print type(json.dumps(r)) # <type 'str'>

    # from pprint import pprint
    # print "Dentro de Apiai"
    # pprint(r)
    # res = requests.post(WebHook_URL, data=json.dumps(r))
    # print type(res.json())
    return res#.json()
