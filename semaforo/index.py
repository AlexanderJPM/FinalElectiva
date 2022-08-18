from dataclasses import dataclass
from http import client
from pydoc import cli
from pymongo import MongoClient


client = MongoClient(
    "mongodb+srv://electiva:electiva@cluster0.lyulc0c.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database("test")
records = db.nom
# new_s = {
#     "name": "Alexander",
#     "Lastname": "Polanco Moreno"
# }
# records.insert_one(new_s)
datos = list(records.find())
for i in range(len(datos)):
    print(datos[i]["name"])