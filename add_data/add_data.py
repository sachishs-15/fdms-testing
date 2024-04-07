import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import bcrypt
import json
import os
from dotenv import load_dotenv
load_dotenv()
import random


def handlePassword(password):
    salt = bcrypt.gensalt(10)
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')


client = MongoClient(os.getenv('MONGOURI'))
db = client['test1']  
collection = db['restaurants'] 
collection.drop()
collection = db['restaurants'] 

with open('data/restaurants.json') as f:
    restaurants = json.load(f)
    restaurants = random.sample(restaurants, 5)
    for restaurant in restaurants:
        restaurant["password"] = handlePassword(restaurant["password"])
    collection.insert_many(restaurants)

print("Restaurant Data inserted successfully!")
    
with open('data/dishes.json') as f:
    dishes = json.load(f)
    
added_dishes = []
db['dishes'].drop()


for restaurant in restaurants:
    dishCount = int(restaurant["dishCount"])
    rt = db['restaurants'].find({"uid": f"{restaurant['uid']}"})
    rt = rt[0]
    restid = f"{rt.get('_id')}"
    
    dishes_sample = random.sample(dishes, dishCount)

    dishes_sample_copy = dishes_sample.copy()

    for dish in dishes_sample_copy:
        dish_cpy = dish.copy()
        dish_cpy["restaurant"] = {}
        dish_cpy["restaurant"] = ObjectId(restid)
        added_dishes.append(dish_cpy)

#print(added_dishes)
# added_dishes = json.dumps(added_dishes)

db['dishes'].insert_many(added_dishes)

print("Dish Data inserted successfully!")


with open('data/deliverers.json') as f:
    deliverers = json.load(f)
    ndeliverers = 5
    deliverers = random.sample(deliverers, ndeliverers)
    for deliverer in deliverers:
        deliverer["password"] = handlePassword(deliverer["password"])
    collection = db['deliverers']
    collection.drop()
    collection.insert_many(deliverers)

print("Deliverer Data inserted successfully!")


with open('data/customers.json') as f:
    customers = json.load(f)
    ncustomers = 5
    customers = random.sample(customers, ncustomers)
    for customer in customers:
        customer["password"] = handlePassword(customer["password"])
    collection = db['customers']
    collection.drop()
    collection.insert_many(customers)

print("Customer Data inserted successfully!")

with open('data/management.json') as f:
    management = json.load(f)
    nmanagement = 5
    management = random.sample(management, nmanagement)
    for manage in management:
        manage["password"] = handlePassword(manage["password"])
    collection = db['managements']
    collection.drop()
    collection.insert_many(management)

print("Management Data inserted successfully!")