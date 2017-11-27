#!/usr/bin/python
# -*- coding: utf-8 -*-

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Librerias
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
import pymongo
from datetime import datetime # Para insertar la fecha actual
import time #Librería con funcionalidades manipular y dar formato a fechas y horas


from variables import *

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Variables
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
try:
    urlMongoDB = URL_de_MongoDB
except Exception as e:
    print time.strftime("%c"), "- Error al cargar la URL del MongoDB: ", type(e), e

# urlMongoDB = "mongodb://valenciaApp:valenciaApp@ds127321.mlab.com:27321/datos_valencia"

client = pymongo.MongoClient(urlMongoDB)
db = client.get_default_database() # Accedemos a la BD donde tenemos las colecciones
dbUsuarios = db.usuarios
dbMensajes = db.mensajes

#msg['from']={'nombre': 'Arnau', '_id': 192224003, 'idioma': 'cast'}


##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Funciónes
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def insertarNuevoUsuario(nombreUsuario, idUsario):
    query = {
        '_id': idUsario,
        'nombre': nombreUsuario,
        'idioma': "Cast",
        'fechaInsercion': datetime.now(),
        'fechaUltimoAcceso': datetime.now(),
        'numPreguntas': 1
    }

    try:
        dbUsuarios.insert_one(query)
    except Exception as e:
        print time.strftime("%c"), "- Error al insertar Usuario: ", type(e), e

def buscarUsuario(idUsario):
    query = {
        '_id': idUsario
    }
    try:
        cursor = dbUsuarios.find_one(query)
    except Exception as e:
        print time.strftime("%c"), "- Error en buscar Usuario: ", type(e), e

    return cursor

def insertarMensaje(mensaje):
    fechaUnix = mensaje['date']
    mensaje['date'] = datetime.fromtimestamp(fechaUnix)

    try:
        dbMensajes.insert_one(mensaje)
    except Exception as e:
        print time.strftime("%c"), "- Error al insertar Mensaje: ", type(e), e

def actualizarUsuario(idUsario):
    query = {
        '_id': idUsario
    }
    update = { '$inc': { 'numPreguntas': 1}, '$set': {'fechaUltimoAcceso': datetime.now()}}

    try:
        dbUsuarios.update_one(query,update)
        return True
    except Exception as e:
        print time.strftime("%c"), "- Error al actualizar usuario: ", type(e), e


def actualizarIdioma(idUsario,idioma):
    query = {
        '_id': idUsario
    }
    update = {'$set': {'idioma': idioma}}
    try:
        result = dbUsuarios.update_one(query,update)
        return True
    except Exception as e:
        print time.strftime("%c"), "- Error al actualizar el idioma: ", type(e), e

def actualizarRespuesta(message_id, chat_id, respuesta, accion):
    query = {
        'chat.id': chat_id,
        'message_id': message_id
    }
    update = {'$set': {'respuesta_accion': accion, 'respuesta_texto':respuesta}}
    try:
        dbMensajes.update_one(query,update)
    except Exception as e:
        print time.strftime("%c"), "- Error al actualizar la respuesta: ", type(e), e
