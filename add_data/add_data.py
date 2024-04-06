import pymongo
from pymongo import MongoClient
import json
import os
from dotenv import load_dotenv
load_dotenv()
import random


client = MongoClient(os.getenv('MONGOURI'))
db = client['test1']  
collection = db['restaurants'] 
collection.drop()
collection = db['restaurants'] 

with open('data/restaurants.json') as f:
    restaurants = json.load(f)
    restaurants = random.sample(restaurants, 5)
    collection.insert_many(restaurants)

print("Restaurant Data inserted successfully!")
    
with open('data/dishes.json') as f:
    dishes = json.load(f)
    
added_dishes = []
db['dishes'].drop()


for restaurant in restaurants:
   # print(restaurant['uid'])
    dishCount = int(restaurant["dishCount"]['$numberInt'])
    rt = db['restaurants'].find({"uid": f"{restaurant['uid']}"})
   # print(rt[0])
    rt = rt[0]
    restid = f"{rt.get('_id')}"
    #print(restid)

    #print(dishCount)
    dishes_sample = random.sample(dishes, dishCount)
    #print(dishes_sample)

    dishes_sample_copy = dishes_sample.copy()

    for dish in dishes_sample_copy:
        dish_cpy = dish.copy()
        dish_cpy["restaurant"] = {}
        dish_cpy["restaurant"]["$oid"] = restid
        added_dishes.append(dish_cpy)
        #db['dishes'].insert_one(dish)

#print(added_dishes)
# added_dishes = json.dumps(added_dishes)

db['dishes'].insert_many(added_dishes)

print("Dish Data inserted successfully!")


with open('data/deliverers.json') as f:
    deliverers = json.load(f)
    ndeliverers = 5
    deliverers = random.sample(deliverers, ndeliverers)
    collection = db['deliverers']
    collection.drop()
    collection.insert_many(deliverers)

print("Deliverer Data inserted successfully!")


with open('data/customers.json') as f:
    customers = json.load(f)
    ncustomers = 5
    customers = random.sample(customers, ncustomers)
    collection = db['customers']
    collection.drop()
    collection.insert_many(customers)

print("Customer Data inserted successfully!")

with open('data/management.json') as f:
    management = json.load(f)
    nmanagement = 5
    management = random.sample(management, nmanagement)
    collection = db['management']
    collection.drop()
    collection.insert_many(management)

print("Management Data inserted successfully!")