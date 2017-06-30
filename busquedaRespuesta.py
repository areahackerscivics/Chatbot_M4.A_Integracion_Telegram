#!/usr/bin/python
# -*- coding: utf-8 -*-

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Librerias
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
from apiai import *
from comunicacionWebhook import *
from textos import *
from DAO import *

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Variables
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
respuesta = ''

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Funciónes
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def obtenerRespuesta(msg,chat_id, idioma, nombreUsuario):
    texto = msg['text'] # Extraemos el contenido del texto
    accion = None
    message_id = msg['message_id']

    respApiai = sendQuery(texto,chat_id, idioma, nombreUsuario)

    # Si la respuesta es correcta
    if respApiai.status_code==200:
        respApiai = respApiai.json() # Convertimos a dic
        accion = respApiai['result']['action']

        if respApiai['result']['metadata']['webhookUsed'] == 'true':
            # Se conecta al WebHook
            respWH = buscarRespuestaWH(respApiai)

            if respWH.status_code==200:
                # Si la respuesta es correcta
                respWH = respWH.json() # Convertimos a dic
                respuesta = respWH['displayText']
            else:
                # Si no tomamos la respuesta por defecto
                if accion == "Complemento.Saludo":
                    respuesta = busquedaTexto("resComplemento.Saludo",idioma)
                elif accion == "input.unknown":
                    respuesta = busquedaTexto("resinput.unknown",idioma)
                else:
                    respuesta = busquedaTexto("resErrorRespWH",idioma)

        else:
            # No tiene que conectarse al WebHook
            respuesta = respApiai['result']['speech']
    else:
        respuesta = busquedaTexto("resErrorRespApiai",idioma)

    # Insertamos en base de datos la respuesta
    actualizarRespuesta(message_id, chat_id, respuesta, accion)
    return respuesta
