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
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed.decode("utf-8")


def generate_test_database():

    client = MongoClient(
        os.getenv("MONGOURI")
    )
    db = client["test"]
    collection = db["restaurants"]
    collection.drop()
    collection = db["restaurants"]

    # add restaurant data
    restaurants = None
    with open("add_data/data/restaurants.json") as f:
        restaurants = json.load(f)
        restaurants = random.sample(restaurants, 5)

        store_rest = json.dumps(restaurants, indent=4)
        with open("add_data/test_data/restaurants.json", "w") as f2:
            f2.write(store_rest)

        for restaurant in restaurants:
            restaurant["password"] = handlePassword(restaurant["password"])
        collection.insert_many(restaurants)

    if __name__ == "__main__":
        print("Restaurant Data inserted successfully!")

    # add dish data
    with open("add_data/data/dishes.json") as f:
        dishes = json.load(f)

    added_dishes = []
    db["dishes"].drop()

    for restaurant in restaurants:
        dishCount = int(restaurant["dishCount"])
        rt = db["restaurants"].find({"uid": f"{restaurant['uid']}"})
        rt = rt[0]
        restid = f"{rt.get('_id')}"

        dishes_sample = random.sample(dishes, dishCount)

        dishes_sample_copy = dishes_sample.copy()

        for dish in dishes_sample_copy:
            dish_cpy = dish.copy()
            dish_cpy["restaurant"] = {}
            dish_cpy["restaurant"] = ObjectId(restid)
            added_dishes.append(dish_cpy)

    # print(added_dishes)
    # added_dishes = json.dumps(added_dishes)

    db["dishes"].insert_many(added_dishes)
    store_dishes = []
    for dish in db["dishes"].find():
        store_dishes.append(dish)
        store_dishes[-1]["uid"] = str(store_dishes[-1]["_id"])
        store_dishes[-1].pop("_id")
        restaurant = db["restaurants"].find({"_id": store_dishes[-1]["restaurant"]})
        restaurant = restaurant[0]
        store_dishes[-1]["restaurant"] = restaurant["uid"]

    store_dishes = json.dumps(store_dishes, indent=4)
    with open("add_data/test_data/dishes.json", "w") as f:
        f.write(store_dishes)

    if __name__ == "__main__":
        print("Dish Data inserted successfully!")

    # add delivery agent data
    deliverers = None
    with open("add_data/data/deliverers.json") as f:
        deliverers = json.load(f)
        ndeliverers = 1
        deliverers = random.sample(deliverers, ndeliverers)

        store_deliverers = json.dumps(deliverers, indent=4)
        with open("add_data/test_data/deliverers.json", "w") as f2:
            f2.write(store_deliverers)

        for deliverer in deliverers:
            deliverer["password"] = handlePassword(deliverer["password"])
        collection = db["deliverers"]
        collection.drop()
        collection.insert_many(deliverers)

    if __name__ == "__main__":
        print("Deliverer Data inserted successfully!")

    # add customer data
    customers = None
    with open("add_data/data/customers.json") as f:
        customers = json.load(f)
        ncustomers = 5
        customers = random.sample(customers, ncustomers)

        store_customers = json.dumps(customers, indent=4)
        with open("add_data/test_data/customers.json", "w") as f2:
            f2.write(store_customers)

        for customer in customers:
            customer["password"] = handlePassword(customer["password"])
        collection = db["customers"]
        collection.drop()
        collection.insert_many(customers)

    if __name__ == "__main__":
        print("Customer Data inserted successfully!")

    # add management data
    management = None
    with open("add_data/data/management.json") as f:
        management = json.load(f)
        nmanagement = 5
        management = random.sample(management, nmanagement)

        store_management = json.dumps(management, indent=4)
        with open("add_data/test_data/management.json", "w") as f2:
            f2.write(store_management)

        for manage in management:
            manage["password"] = handlePassword(manage["password"])
        collection = db["managements"]
        collection.drop()
        collection.insert_many(management)

    if __name__ == "__main__":
        print("Management Data inserted successfully!")

    # clear the orders collection
    db["orders"].drop()

    print("Test data inserted successfully!")


if __name__ == "__main__":

    generate_test_database()
