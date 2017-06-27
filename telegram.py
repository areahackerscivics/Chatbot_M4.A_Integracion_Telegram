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
from DAO import *
from botonesTeclados import *


##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Variables
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
try:
    TOKEN = os.environ['BOT_ACCESS_TOKEN']
    # activo = os.environ['activo']

except:
    print "Error al cargar token de Telegram"


# TECLADOS -----------------------------------------------------------------------------------------------------------------------------------------------------------
tecladoIdioma = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Valencià', callback_data='Val'),
     InlineKeyboardButton(text='Castellano', callback_data='Cast')],#Dentro de la lista para que se vea en la misma línea
    ])

# Diccionario para hacer el Case en Python --------------------------------------------------------------------------------------------------------------------------
# Cada nuevo boton añadir un key: <nombre_función>
funcionBoton = { # Las funciones se encuentran en: "from botonesTeclados import *"
    "Cast": idiomaCast,
    "Val": idiomaVal
    } # Tiene que estar al final de las funciones que pretendemos llamar

# TEXTOS --------------------------------------------------------------------------------------------------------------------------------------------------
botInactivo = "¡Huy, ahora mismo estoy en mantenimiento! Vuelve a hablarme más tarde por favor."
comandoStart = 'Hola, es la primera vez que entras. ¿En qué idioma quieres que me comunique contigo?'
usuarioNoGuardado = 'Hola parece que ha habido un error y no tengo almacenado en que idioma quieres que me comunique contigo. ¿Me lo podrías recordar?'
errorNoTexto = "Perdona pero no entiendo este tipo de mensajes."
comandoIdioma = "¿En qué idioma quieres que me comunique contigo a partir de ahora?"


##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Funciónes
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Si el mensaje recibido se tratara de un chat ------------------------------------------------------------------------------------------------------------------------
def on_chat_message(msg):
    insertarMensaje(msg) # Insertamos el mensaje recibido en la BD

    content_type, chat_type, chat_id = telepot.glance(msg)
                # - content_type: tipo de contenido del mensaje (text, etc.)
                # - chat_type: por ahora siempre es private
                # - chat_id: identificador único del chat al que responderemos

    if activo == False:
        actualizarUsuario(chat_id)
        bot.sendMessage(chat_id, botInactivo)
        return
    # print content_type, chat_type, chat_id
    # print msg

    # Solo dejamos entrar los mensajes que son tipo text
    if content_type == "text" and msg.has_key('text'):
        # Buscamos si el texto recibido es una entidad 'comando' y de ser así cual es
        if msg.has_key('entities'):
            entidades = msg['entities']
            for entidad in entidades:
                if entidad['type'] == "bot_command":
                    comando = msg['text'][0:entidad['length']]
                    entidad="bot_command"
                    break
        else:
            entidad = ''
            comando = ''
        # Si tiene remitente sacamos su nombre, si no le llamamos 'Ciudadano'
        if msg.has_key('from'):
            nombreUsuario = msg['from']['first_name'] # Guardamos la variable de el nombre del usuario que se conecta
            idUsario = msg['from']['id']
        else:
            nombreUsuario = 'Ciudadano'
            idUsario = 0
        # COMANDOS -----------------------------------------------------------------------------------------------
        if entidad == 'bot_command':
            if comando == '/start':
                insertarNuevoUsuario(nombreUsuario,idUsario)
                bot.sendMessage(chat_id, comandoStart, reply_markup=tecladoIdioma)
            elif comando == '/idioma':
                bot.sendMessage(chat_id, comandoIdioma, reply_markup=tecladoIdioma)

            # elif comando == '': # Añadir comandos
        # ----------------------------------------------------------------------------------------------- COMANDOS

        else:
            # Extraemos el contenido del texto
            texto = msg['text']
            usuario = buscarUsuario(idUsario)

            # usuario = [{u'fechaInsercion': datetime.datetime(2017, 6, 26, 11, 42, 53, 295000), u'fechaUltimoAcceso': datetime.datetime(2017, 6, 27, 11, 14, 25, 415000), u'_id': 192224003, u'nombre': u'Arnau', u'idioma': u'Val', u'numPreguntas': 2}]

            if usuario == None: # Usuario no existe
                insertarNuevoUsuario(nombreUsuario,idUsario)
                bot.sendMessage(chat_id, usuarioNoGuardado, reply_markup=tecladoIdioma)
            else: # Usuario existe
                actualizarUsuario(idUsario)


            respuesta = obtenerRespuesta(texto,chat_id) # Buscamos respuesta

            bot.sendMessage(chat_id, respuesta) # Enviamos respuesta
    else:
        bot.sendMessage(chat_id, errorNoTexto)


# Si el mensaje recibido se tratara de un respuesta CALLBACK (de un teclado) -----------------------------------------------------------------------------------------
def on_callback_query(msg):
    # print "Dentro de on_callback_query"
    query_id, idUsuario, query_data = telepot.glance(msg, flavor='callback_query')  #query_id: ID de la query
                                                                                    #from_id: ID de usuario que realiza la petición
                                                                                    #query_data: String diferenciador seleccionado para cada botón
    # print'Callback Query: query_id:', query_id,',from_id: ',  idUsuario, ', query_data: ', query_data

    funcionBoton[query_data](bot, query_id, idUsuario, query_data)


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
