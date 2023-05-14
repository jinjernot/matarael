import pymongo
import data.passwords as passwords
import os
import json

pw = passwords.mongodbPassword

connection_string = "mongodb+srv://norindes:{}@jinjernot.mhqetpj.mongodb.net/".format(pw)

client = pymongo.MongoClient(connection_string)
database = client.get_database("matarael")
collection = database.get_collection("techspecs")

path = "json"
json_data_list = []
for file in os.listdir(path):
    if "facet" not in file:

        with open(os.path.join(path, file)) as f:
            json_data = json.load(f)
        json_data_list.append(json_data)

for json_data in json_data_list:
    collection.insert_one(json_data)

documents = collection.find()

for document in documents:
    print(document)