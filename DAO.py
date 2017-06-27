#!/usr/bin/python
# -*- coding: utf-8 -*-

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Librerias
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
import pymongo
from datetime import datetime # Para insertar la fecha actual

from variables import *

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Variables
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
try:
    urlMongoDB = os.environ['URL_de_MongoDB']
except:
    print "Error al cargar la URL del MongoDB"

# urlMongoDB = "mongodb://valenciaApp:valenciaApp@ds127321.mlab.com:27321/datos_valencia"

client = pymongo.MongoClient(urlMongoDB)
db = client.get_default_database() # Accedemos a la BD donde tenemos las colecciones
dbUsuarios = db.usuarios
dbMensajes = db.mensajes

#msg['from']={'nombre': 'Arnau', '_id': 192224003, 'idioma': 'cast'}

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
    except:
        print "Error al insertar Usuario"

def buscarUsuario(idUsario):
    query = {
        '_id': idUsario
    }
    try:
        cursor = dbUsuarios.find_one(query)
    except:
        print "Error en buscar Usuario"

    return cursor

def insertarMensaje(mensaje):
    try:
        dbMensajes.insert_one(mensaje)
    except:
        print 'Error al insertar Mensaje'

def actualizarUsuario(idUsario):
    query = {
        '_id': idUsario
    }
    update = { '$inc': { 'numPreguntas': 1}, '$set': {'fechaUltimoAcceso': datetime.now()}}

    try:
        dbUsuarios.update_one(query,update)
        return True
    except:
        print "Error al actualizar el idioma"


def actualizarIdioma(idUsario,idioma):
    query = {
        '_id': idUsario
    }
    update = {'$set': {'idioma': idioma}}
    try:
        result = dbUsuarios.update_one(query,update)
        return True
    except:
        print "Error al actualizar el idioma"



# # /////////////////////////////
# msg = {}
# msg['from']={'first_name': 'Arnau', 'id': 192224003}
#
# # if buscarUsuario(msg)==[]:
# #     print "nuevo"
# #     insertarNuevoUsuario(msg)
# # else:
# #     print "EXISTE"
# insertarNuevoUsuario(msg)
