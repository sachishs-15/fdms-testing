from pymongo import MongoClient
from bson.objectid import ObjectId
import bcrypt
import json
import os
from dotenv import load_dotenv

load_dotenv()


def handlePassword(password):
    salt = bcrypt.gensalt(10)
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed.decode("utf-8")


client = MongoClient(os.getenv("MONGOURI"))
db = client[os.getenv("TEST_DB_NAME")]

with open("add_data/data/delivery-agent.json") as f:
    delivery_agent = json.load(f)
    delivery_agent["password"] = handlePassword(delivery_agent["password"])
    print(delivery_agent)
    db["deliverers"].drop()
    db["deliverers"].insert_many([delivery_agent])
