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

# try:
#     WebHook_URL = WebHook_URL
# except Exception as e:
#     print time.strftime("%c"), "- Error al cargar la URL del WebHook: ", type(e), e


def buscarRespuestaWH(r):
    """La variable 'resultado' será pasado como diccionario con
    el esquema de respuesta de api.ai. Solo se llamara a la
    función cuando webhookUsed = 'true' """

    res = requests.post(WebHook_URL, data=json.dumps(r))

    return res
