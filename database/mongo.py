import pymongo
import database.passwords as passwords

def connect():

    pw = passwords.mongodbPassword
    connection_string = "mongodb+srv://norindes:{}@jinjernot.mhqetpj.mongodb.net/".format(pw)
    
    client = pymongo.MongoClient(connection_string, connectTimeoutMS=30000, socketTimeoutMS=None, connect=False, maxPoolsize=1
)
    db = client.get_database("matarael")
    collection = db.get_collection("techspecs")
    
    return collection

