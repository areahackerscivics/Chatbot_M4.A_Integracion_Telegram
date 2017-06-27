#!/usr/bin/python
# -*- coding: utf-8 -*-


##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Librerias
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
import telepot #Framework para Telegram Bot API
from DAO import *

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Variables
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
textAlPulsarCast = 'Guardado en memoria.'
respuestaCambioIdiomaCast = 'A partir de ahora las comunicaciones serán en castellano.'
respuestaCambioIdiomaCastError = 'No se pudo guardar el cambio en estos momentos, vuelve a intentarlo más tarde por favor.'


textAlPulsarVal = "Guardat en memòria."
respuestaCambioIdiomaVal = "A partir d'ara les comunicacions seran en valencià."
respuestaCambioIdiomaValError = "No s'ha pogut desar el canvi ara mateix, torna a intentar-ho més tard si us plau."


def idiomaCast(bot, query_id, idUsuario, query_data):
    # Actualizar los datos de idioma
    resultado = actualizarIdioma(idUsuario, query_data)

    if resultado == True:
        bot.answerCallbackQuery(query_id, text=textAlPulsarCast)
        bot.sendMessage(idUsuario, respuestaCambioIdiomaCast)
    else:
        bot.sendMessage(idUsuario, respuestaCambioIdiomaCastError)


def idiomaVal(bot, query_id, idUsuario, query_data):
    # Actualizar los datos de idioma
    resultado = actualizarIdioma(idUsuario, query_data)

    if resultado == True:
        bot.answerCallbackQuery(query_id, text=textAlPulsarVal)
        bot.sendMessage(idUsuario, respuestaCambioIdiomaVal)
    else:
        bot.sendMessage(idUsuario, respuestaCambioIdiomaValError)
