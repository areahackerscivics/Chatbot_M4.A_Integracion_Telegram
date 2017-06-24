#!/usr/bin/python
# -*- coding: utf-8 -*-


##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Librerias
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
import telepot #Framework para Telegram Bot API

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Variables
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
textAlPulsarCast = 'Guardado en memoria'
respuestaCambioIdiomaCast = 'A partir de ahora las comunicaciones serán en castellano'


textAlPulsarVal = "Guardat en memòria"
respuestaCambioIdiomaVal = "A partir d'ara les comunicacions seran en valencià"


def idiomaCast(bot, query_id, from_id, query_data):
    print "Cast"
    # Actualizar los datos de idioma
    bot.answerCallbackQuery(query_id, text=textAlPulsarCast)
    bot.sendMessage(from_id, respuestaCambioIdiomaCast)

def idiomaVal(bot, query_id, from_id, query_data):
    print "Val"
    # Actualizar los datos de idioma
    bot.answerCallbackQuery(query_id, text=textAlPulsarVal)
    bot.sendMessage(from_id, respuestaCambioIdiomaVal)
