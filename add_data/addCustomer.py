import pymongo
from pymongo import MongoClient
import json
import os
from dotenv import load_dotenv
load_dotenv()

client = MongoClient(os.getenv('MONGOURI'))
db = client['test']  
collection = db['customers']  

with open('data.json') as f:
    data = json.load(f)

collection.insert_many(data)

print("Data inserted successfully!")
