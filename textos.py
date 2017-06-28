#!/usr/bin/python
# -*- coding: utf-8 -*-

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Librerias
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------


##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Variables
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
dicVal = {
# telegram.py //////////////////////////////////////////////////////////////////
    "botInactivo": "Huy, ara mateix estic en manteniment! Torna a parlar-me més tard per favor.",
    "comandoStart": "Hola, és la primera vegada que entres. En quin idioma vols que em comunique amb tu?",
    "comandoIdioma": "En quin idioma vols que em comunique amb tu a partir d'ara?",
    "usuarioNoGuardado": "Hola sembla que hi ha hagut un error i no tinc emmagatzemat que idioma vols que em comunique amb tu. M'ho podries recordar?",
    "errorNoTexto": "Perdona però no entenc aquest tipus de missatges.",
# busquedaRespuesta.py /////////////////////////////////////////////////////////
    "resErrorRespApiai": 'El servei està caigut ara mateix, torna a intentar-ho més tard.',
# botonesTeclados.py ///////////////////////////////////////////////////////////
    "pulsarBotonIdioma": "Guardat en memòria.",
    "respuestaCambioIdioma": "A partir d'ara les comunicacions seran en valencià.",
    "respuestaCambioIdiomaError": "No s'ha pogut desar el canvi ara mateix, torna a intentar-ho més tard si us plau."
}

dicCast = {
# telegram.py //////////////////////////////////////////////////////////////////
    "botInactivo": "¡Huy, ahora mismo estoy en mantenimiento! Vuelve a hablarme más tarde por favor.",
    "comandoStart": 'Hola, es la primera vez que entras. ¿En qué idioma quieres que me comunique contigo?',
    "comandoIdioma": "¿En qué idioma quieres que me comunique contigo a partir de ahora?",
    "usuarioNoGuardado": 'Hola parece que ha habido un error y no tengo almacenado en que idioma quieres que me comunique contigo. ¿Me lo podrías recordar?',
    "errorNoTexto": "Perdona pero no entiendo este tipo de mensajes.",
# busquedaRespuesta.py /////////////////////////////////////////////////////////
    "resErrorRespApiai": 'El servicio esta caído ahora mismo, vuelve a intentarlo más tarde.',
# botonesTeclados.py ///////////////////////////////////////////////////////////
    "pulsarBotonIdioma": 'Guardado en memoria.',
    "respuestaCambioIdioma": 'A partir de ahora las comunicaciones serán en castellano.',
    "respuestaCambioIdiomaError": 'No se pudo guardar el cambio en estos momentos, vuelve a intentarlo más tarde por favor.'
}

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Función
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def busquedaTexto(key,idioma):
    if idioma == 'Val':
        text = dicVal[key]

    else:
        text = dicCast[key]

    return text
