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

#msg['from']={'nombre': 'Arnau', '_id': 192224003, 'idioma': 'cast'}

def insertarNuevoUsuario(mensaje):
    usuario = mensaje['from']

    query = {
        '_id': usuario['id'],
        'nombre': usuario['first_name'],
        'idioma': "Cast",
        'fechaInsercion': datetime.now()
    }

    try:
        dbUsuarios.insert_one(query)
    except:
        print "Error al insertar Usuario"

def buscarUsuario(mensaje):
    usuarioID = mensaje['from']['id']
    query = {
        '_id': usuarioID
    }
    try:
        cursor = list(dbUsuarios.find(query))
    except:
        print "Error en buscar Usuario"

    return cursor


# /////////////////////////////
msg = {}
msg['from']={'first_name': 'Arnau', 'id': 192224003}

# if buscarUsuario(msg)==[]:
#     print "nuevo"
#     insertarNuevoUsuario(msg)
# else:
#     print "EXISTE"
insertarNuevoUsuario(msg)
