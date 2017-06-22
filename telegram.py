#!/usr/bin/python
# -*- coding: utf-8 -*-

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Librerias
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
import telepot #Framework para Telegram Bot API
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton #Incluye las funcionalidades para crear teclados personalizados

import time #Librería con funcionalidades manipular y dar formato a fechas y horas

# Mis funciones
# from apiai import *
from variables import *
# from comunicacionWebhook import *
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
    print "Chat"
    content_type, chat_type, chat_id = telepot.glance(msg)
    # - chat_id: identificador único del chat al que responderemos
    # - content_type: tipo de contenido del mensaje (text, etc.)
    # - chat_type: por ahora siempre es private

    print content_type, chat_type, chat_id

    # El mensaje puede no tener remitente, en caso que sea así nos referiremos
    # como Ciudadano
    try:
        nombreUsuario = msg['from']['first_name'] # Guardamos la variable de el nombre del usuario que se conecta
        idUsario = msg['from']['id']
    except:
        nombreUsuario = 'Ciudadano'
        idUsario = 0
    if content_type == "text":
        bot.sendMessage(chat_id, "Hola")
    else:
        pass


# Si el mensaje recibido se tratara de un respuesta CALLBACK (de un teclado) -----------------------------------------------------------------------------------------
def on_callback_query(msg):
    print "B"


# Si el mensaje recibido se tratara de un respuesta inline query (NO vamos a usar por ahora) -------------------------------------------------------------------------
def on_inline_query(msg):
    print "Entro inline"


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
