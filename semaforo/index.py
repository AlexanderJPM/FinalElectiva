from dataclasses import dataclass
from http import client
from pydoc import cli
from pymongo import MongoClient


class mongo():
    client = MongoClient(
        "mongodb+srv://electiva:electiva@cluster0.lyulc0c.mongodb.net/?retryWrites=true&w=majority")
    db = client.get_database("test")
    records = db.nom
    vadd = 23

    def countCollection(self):
        return (len(list(self.records.find())))

    def getCollection(self, id):
        loadData = list(self.records.find())
        listed = []
        listed.append(loadData[id]["Metros"])
        listed.append(loadData[id]["Color"])
        listed.append(loadData[id]["IP"])
        return (listed)

    def insertCollection(self, color, Ip):
        new_s = {
            "Metros": "10",
            "Color": color,
            "IP": Ip
        }
        self.records.insert_one(new_s)


# mongo = mongo()
# datos = mongo.getCollection(1)
# print(datos[0])


# records = db.nom

# records.insert_one(new_s)
# datos =
# for i in range(len(datos)):
#     print(datos[i]["name"])
