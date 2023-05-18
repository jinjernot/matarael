import pymongo
import database.passwords as passwords

def connect():

    pw = passwords.mongodbPassword
    connection_string = "mongodb+srv://norindes:{}@jinjernot.mhqetpj.mongodb.net/".format(pw)
    
    client = pymongo.MongoClient(connection_string)
    db = client.get_database("matarael")
    collection = db.get_collection("techspecs")
    
    return collection

