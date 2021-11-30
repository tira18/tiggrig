from pymongo import MongoClient

# Replace these with your server details
MONGO_HOST = "localhost" 
MONGO_PORT = "27017"
MONGO_DB = "tc_chat_module_qa"
MONGO_USER = "admin"
MONGO_PASS = "admin"

uri = "mongodb://{}:{}@{}:{}/{}?authSource=admin".format(MONGO_USER, MONGO_PASS, MONGO_HOST, MONGO_PORT, MONGO_DB)
client = MongoClient(uri)
for db in client.list_databases():
    print(db)
