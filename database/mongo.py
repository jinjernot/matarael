import pymongo
import database.passwords as passwords

def connect():

    pw = passwords.mongodbPassword
    connection_string = "mongodb+srv://norindes:{}@jinjernot.mhqetpj.mongodb.net/".format(pw)
    
    client = pymongo.MongoClient(connection_string)
    database = client.get_database("matarael")
    collection = database.get_collection("techspecs")

    for document in collection.find():
        print(document)

    return collection

collection = connect()

