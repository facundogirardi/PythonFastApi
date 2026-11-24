### MongoDB client ###

# Descarga versión community: https://www.mongodb.com/try/download
# Instalación:https://www.mongodb.com/docs/manual/tutorial
# Módulo conexión MongoDB: pip install pymongo
# Ejecución: sudo mongod --dbpath "/path/a/la/base/de/datos/"
# Conexión: mongodb://localhost

import os

from pymongo import MongoClient

# La URI de conexión se toma de la variable de entorno MONGODB_URI.
# Por defecto usa un MongoDB local (mongodb://localhost:27017).
# Ejemplo para MongoDB Atlas:
#   MONGODB_URI="mongodb+srv://<user>:<password>@<url>/?retryWrites=true&w=majority"
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
MONGODB_DB = os.getenv("MONGODB_DB", "test")

db_client = MongoClient(MONGODB_URI)[MONGODB_DB]
