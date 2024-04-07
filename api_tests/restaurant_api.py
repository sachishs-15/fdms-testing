import os
import json
import random
from dotenv import load_dotenv

import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helpers.BaseRequest import get, post, put, delete

load_dotenv()

BACKEND_API_URL = os.getenv("BACKEND_API_URL", "http://localhost:3000")

token = ""
dishID = ""


def restaurantLogin(email, password, status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/restaurant/login"
    data = {"email": email, "password": password}

    schema = {
        "type": "object",
        "properties": {"success": {"type": "boolean"}, "token": {"type": "string"}},
    }

    try:
        global token
        response = post(
            url, headers={}, data=data, status_code=status_code, schema=schema
        )
        if "token" in response:
            token = response["token"]
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False

    print(testMsg + "PASSED")
    return True


def restaurantSignup(
    name, email, phone, password, address, timings, tags, status_code=200, testMsg=""
):
    url = f"{BACKEND_API_URL}/restaurant/signup"
    data = {
        "email": email,
        "password": password,
        "name": name,
        "phone": phone,
        "address": address,
        "timings": timings,
        "tags": tags,
    }

    schema = {
        "type": "object",
        "properties": {"success": {"type": "boolean"}, "token": {"type": "string"}},
    }

    try:
        global token
        response = post(
            url, headers={}, data=data, status_code=status_code, schema=schema
        )
        if "token" in response:
            token = response["token"]
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False

    print(testMsg + "PASSED")
    return True


def restaurantInfo(status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/restaurant/info"
    headers = {"Authorization": f"Bearer {token}"}
    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "email": {"type": "string"},
            "phone": {"type": "string"},
            "address": {"type": "string"},
            "timings": {"type": "object"},
            "tags": {"type": "array"},
            "image": {"type": "string"},
        },
        "required": ["name", "email", "phone", "address", "timings", "tags"],
    }

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False

    print(testMsg + "PASSED")
    return True


def restaurantEditInfo(
    name, phone, address, timings, tags, status_code=200, testMsg=""
):
    url = f"{BACKEND_API_URL}/restaurant/info"
    headers = {"Authorization": f"Bearer {token}"}

    data = {
        "name": name,
        "phone": phone,
        "address": address,
        "timings": timings,
        "tags": tags,
    }

    schema = {
        "type": "object",
        "properties": {
            "success": {"type": "boolean"},
        },
        "required": ["success"],
    }

    try:
        response = put(
            url, headers=headers, data=data, status_code=status_code, schema=schema
        )
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False

    print(testMsg + "PASSED")
    return True


# IMAGE UPLOAD


def restaurantOrders(status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/restaurant/orders"

    headers = {"Authorization": f"Bearer {token}"}

    schema = {"type": "array"}

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False

    print(testMsg + "PASSED")
    return True


def restaurantOrderByID(order_id, status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/restaurant/orders/{order_id}"

    headers = {"Authorization": f"Bearer {token}"}

    schema = {
        "type": "object",
        "properties": {
            "uid": {"type": "string"},
            "restaurant": {"type": "object"},
            "delivery_agent": {"type": "object"},
            "items": {"type": "array"},
            "total": {"type": "number"},
            "status": {"type": "string"},
            "isCompleted": {"type": "boolean"},
        },
        "required": [
            "uid",
            "restaurant",
            "items",
            "total",
            "status",
            "delivery_agent",
            "isCompleted",
        ],
    }

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False

    print(testMsg + "PASSED")
    return True


def restaurantMenu(status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/restaurant/menu"

    headers = {"Authorization": f"Bearer {token}"}

    schema = {"type": "array"}

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False

    print(testMsg + "PASSED")
    return True


def restaurantAddFoodItem(name, price, status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/restaurant/menu"

    headers = {"Authorization": f"Bearer {token}"}

    data = {"name": name, "price": price}

    schema = {
        "type": "object",
        "properties": {"uid": {"type": "string"}},
        "required": ["uid"],
    }

    try:
        response = post(
            url, headers=headers, data=data, status_code=status_code, schema=schema
        )
        global dishID
        dishID = response["uid"]
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False

    print(testMsg + "PASSED")
    return True


def restaurantFoodItem(uid, status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/restaurant/menu/{uid}"

    headers = {"Authorization": f"Bearer {token}"}

    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "price": {"type": "number"},
            "isAvailable": {"type": "boolean"},
        },
        "required": ["name", "price", "isAvailable"],
    }

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False

    print(testMsg + "PASSED")
    return True


def restaurantRemoveFoodItem(uid, status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/restaurant/menu/{uid}"

    headers = {"Authorization": f"Bearer {token}"}

    schema = {
        "type": "object",
        "properties": {"message": {"type": "string"}},
        "required": ["message"],
    }

    try:
        response = delete(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False

    print(testMsg + "PASSED")
    return True


def restaurantUpdateFoodItem(
    uid, name, price, isAvailable, status_code=200, testMsg=""
):
    url = f"{BACKEND_API_URL}/restaurant/menu/{uid}"

    headers = {"Authorization": f"Bearer {token}"}

    data = {"name": name, "price": price, "isAvailable": isAvailable}

    schema = {
        "type": "object",
        "properties": {"message": {"type": "string"}},
    }

    try:
        response = put(
            url, headers=headers, data=data, status_code=status_code, schema=schema
        )
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False

    print(testMsg + "PASSED")
    return True


# FOOD ITEM IMAGE


def restaurantReviews(status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/restaurant/reviews"

    headers = {"Authorization": f"Bearer {token}"}

    schema = {"type": "array"}

    try:
        response = post(
            url, headers=headers, data={}, status_code=status_code, schema=schema
        )
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False

    print(testMsg + "PASSED")
    return True


parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CREATION_DATA_PATH = os.path.join(parent_directory, "creation_data", "restaurants.json")
REST_DATA_PATH = os.path.join(
    parent_directory, "add_data", "test_data", "restaurants.json"
)


def run_restaurant_tests():
    tests_conducted = 0
    count = 0

    restaurants = json.load(open(CREATION_DATA_PATH))
    restaurant = restaurants[random.randint(0, len(restaurants) - 1)]
    # print(restaurant)

    print("Running Restaurant API tests...")

    tests_conducted += 1
    if restaurantSignup(
        restaurant["name"],
        restaurant["email"],
        restaurant["phone"],
        restaurant["password"],
        restaurant["address"],
        restaurant["timings"],
        restaurant["tags"],
        status_code=201,
        testMsg="Successful Restaurant signup test: ",
    ):
        count += 1

    tests_conducted += 1
    if restaurantSignup(
        restaurant["name"],
        restaurant["email"],
        restaurant["phone"],
        restaurant["password"],
        restaurant["address"],
        restaurant["timings"],
        restaurant["tags"],
        status_code=406,
        testMsg="Duplicate Restaurant signup test: ",
    ):
        count += 1

    restaurants = json.load(open(REST_DATA_PATH))
    restaurant = restaurants[random.randint(0, len(restaurants) - 1)]

    tests_conducted += 1
    if restaurantLogin(
        restaurant["email"],
        restaurant["password"],
        status_code=200,
        testMsg="Restaurant Login test: ",
    ):
        count += 1

    tests_conducted += 1
    if restaurantLogin(
        restaurant["email"],
        "wrongpassword",
        status_code=400,
        testMsg="Incorrect Password test: ",
    ):
        count += 1

    tests_conducted += 1
    if restaurantInfo(status_code=200, testMsg="Restaurant Info test: "):
        count += 1

    tests_conducted += 1
    if restaurantMenu(status_code=200, testMsg="Restaurant Menu test: "):
        count += 1

    tests_conducted += 1
    if restaurantOrders(status_code=200, testMsg="Restaurant Orders test: "):
        count += 1

    tests_conducted += 1
    if restaurantReviews(status_code=200, testMsg="Restaurant Reviews test: "):
        count += 1

    tests_conducted += 1
    if restaurantAddFoodItem(
        "Test Dish", 100, status_code=200, testMsg="Add Dish test: "
    ):
        count += 1

    tests_conducted += 1
    if restaurantUpdateFoodItem(
        dishID,
        "Test Dish Edit",
        100,
        True,
        status_code=200,
        testMsg="Update Dish test: ",
    ):
        count += 1

    tests_conducted += 1
    if restaurantRemoveFoodItem(dishID, status_code=200, testMsg="Remove Dish test: "):
        count += 1

    print(f"{count}/{tests_conducted} tests passed.\n")


if __name__ == "__main__":

    run_restaurant_tests()
