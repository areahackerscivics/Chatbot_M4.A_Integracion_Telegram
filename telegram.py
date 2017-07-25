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
from textos import *


##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Variables
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
try:
    TOKEN = os.environ['BOT_ACCESS_TOKEN']
except Exception as e:
    print time.strftime("%c"), "- Error al cargar token de Telegram: ", type(e), e


# TECLADOS ---------------------------------------------------------------------
tecladoIdioma = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Valencià', callback_data='Val'),
     InlineKeyboardButton(text='Castellano', callback_data='Cast')],#Dentro de la lista para que se vea en la misma línea
    ])
# --------------------------------------------------------------------- TECLADOS

# CASE -------------------------------------------------------------------------
# Diccionario para hacer el Case en Python (Cada nuevo boton añadir un key: <nombre_función>)
funcionBoton = {        # Las funciones se encuentran en: "from botonesTeclados import *"
    "Cast": idiomaCast,
    "Val": idiomaVal
    }                   # Tiene que estar al final de las funciones que pretendemos llamar
# ------------------------------------------------------------------------- CASE

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Funciónes
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Si el mensaje recibido se tratara de un chat ------------------------------------------------------------------------------------------------------------------------
def on_chat_message(msg):
    insertarMensaje(msg) # Insertamos el mensaje recibido en la BD

    # EXTRACCIÓN INFORMACIÓN MENSAJE -------------------------------------------
    content_type, chat_type, chat_id = telepot.glance(msg)
                # - content_type: tipo de contenido del mensaje (text, etc.)
                # - chat_type: por ahora siempre es private
                # - chat_id: identificador único del chat al que responderemos

    idUsario = chat_id # Para usuarios normales el valor es el mismo

    usuario = buscarUsuario(idUsario) # Consultamos los datos del usuario

    if usuario == None: # USUARIO NO EXISTE
        if msg.has_key('from'):
            nombreUsuario = msg['from']['first_name'] # Guardamos la variable de el nombre del usuario que se conecta
        else:
            nombreUsuario = 'Ciudadano'

        insertarNuevoUsuario(nombreUsuario,idUsario)
        bot.sendMessage(chat_id, busquedaTexto('usuarioNoGuardado','Val'))
        bot.sendMessage(chat_id, busquedaTexto('usuarioNoGuardado','Cast'), reply_markup=tecladoIdioma)
        return # Fin

    else: # USUARIO EXISTE
        actualizarUsuario(idUsario)

        if usuario.has_key('idioma') and usuario.has_key('nombre'):
            idioma = usuario['idioma']
            nombreUsuario = usuario['nombre']
        else:
            idioma = 'Cast'
            nombreUsuario = 'Ciudadano'
    # ------------------------------------------- EXTRACCIÓN INFORMACIÓN MENSAJE

    # COMANDOS -----------------------------------------------------------------
    # Búsqueda si el mensaje es un comando
    if msg.has_key('entities') and msg.has_key('text'):
        entidades = msg['entities']
        for entidad in entidades:
            if entidad['type'] == "bot_command":
                comando = msg['text'][0:entidad['length']]
                entidad="bot_command"
                break
    else:
        entidad = ''
        comando = ''

    # Respuesta del mensaje
    if entidad == 'bot_command':
        if comando == '/start':
            insertarNuevoUsuario(nombreUsuario,idUsario)
            bot.sendMessage(chat_id, busquedaTexto('comandoStart','Val'))
            bot.sendMessage(chat_id, busquedaTexto('comandoStart','Cast'), reply_markup=tecladoIdioma)
            return # Fin
        elif comando == '/idioma':
            bot.sendMessage(chat_id, busquedaTexto('comandoIdioma',idioma), reply_markup=tecladoIdioma)
            return # Fin
        # elif comando == '': # Añadir comandos
    # ----------------------------------------------------------------- COMANDOS

    # ACTIVO -------------------------------------------------------------------
    if activo == False:
        bot.sendMessage(chat_id, busquedaTexto('botInactivo',idioma))
        return # Fin
    # ------------------------------------------------------------------- ACTIVO

    # RESPUESTA ----------------------------------------------------------------
    if content_type == "text" and msg.has_key('text') and entidad != 'bot_command': # ENTRADA TEXTUAL


        respuesta = obtenerRespuesta(msg, chat_id, idioma, nombreUsuario) # Buscamos respuesta

        bot.sendMessage(chat_id, respuesta) # Enviamos respuesta

    else: # ENTRADA NO TEXTUAL
        bot.sendMessage(chat_id, busquedaTexto('errorNoTexto',idioma))
    # ---------------------------------------------------------------- RESPUESTA


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

bot = telepot.Bot(TOKEN)    # Creamos el escuchador del bot con el TOKEN

bot.message_loop({'chat': on_chat_message,
                  'callback_query': on_callback_query,
                  'inline_query':on_inline_query}) # Iniciamos el escuchador del bot

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Mantiene el programa ejecutándose
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------

print time.strftime("%c"), '-> Listening ...'   # En consola indica que ya está en ejecución
while 1:
    time.sleep(10)      # Impide el avance durante 10 segundos
    print time.strftime("%c")
