#!/usr/bin/python
# -*- coding: utf-8 -*-

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Librerias
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
import telepot #Framework para Telegram Bot API
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton #Incluye las funcionalidades para crear teclados personalizados

import time #Librería con funcionalidades manipular y dar formato a fechas y horas

# Mis funciones
from busquedaRespuesta import *
from variables import *
# from DAO import *

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Variables
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
try:
    TOKEN = os.environ['BOT_ACCESS_TOKEN']

except:
    print "Error al cargar token de Telegram"


# TECLADOS -----------------------------------------------------------------------------------------------------------------------------------------------------------
tecladoIdioma = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Valencià', callback_data='Val'),
     InlineKeyboardButton(text='Castellano', callback_data='Cast')],#Dentro de la lista para que se vea en la misma línea
    ])


##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Funciónes
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Si el mensaje recibido se tratara de un chat ------------------------------------------------------------------------------------------------------------------------
def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    # - content_type: tipo de contenido del mensaje (text, etc.)
    # - chat_type: por ahora siempre es private
    # - chat_id: identificador único del chat al que responderemos

    print content_type, chat_type, chat_id

    # Si tiene remitente sacamos su nombre, si no le llamamos 'Ciudadano'
    if msg.has_key('from'):
        nombreUsuario = msg['from']['first_name'] # Guardamos la variable de el nombre del usuario que se conecta
        idUsario = msg['from']['id']
    else:
        nombreUsuario = 'Ciudadano'
        idUsario = 0

    # Solo dejamos entrar los mensajes que son tipo text
    if content_type == "text" and msg.has_key('text'):

        texto = msg['text']

        respuesta = obtenerRespuesta(texto)

        bot.sendMessage(chat_id, respuesta)
    else:
        bot.sendMessage(chat_id, "Perdona pero no entiendo este tipo de mensajes.")


# Si el mensaje recibido se tratara de un respuesta CALLBACK (de un teclado) -----------------------------------------------------------------------------------------
def on_callback_query(msg):
    print "Dentro de on_callback_query"


# Si el mensaje recibido se tratara de un respuesta inline query (NO vamos a usar por ahora) -------------------------------------------------------------------------
def on_inline_query(msg):
    print "Dentro de on_inline_query"


##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Inicio bot
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------

bot = telepot.Bot(TOKEN)    # Creamos el escuchador del bot con id=TOKEN
##bot.message_loop(handle)  # Iniciamos el escuchador del bot
bot.message_loop({'chat': on_chat_message,
                  'callback_query': on_callback_query,
                  'inline_query':on_inline_query})

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Mantiene el programa ejecutándose
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------

print 'Listening ...'   # En consola indica que ya está en ejecución
while 1:
    time.sleep(10)      # Impide el avance durante 10 segundos
