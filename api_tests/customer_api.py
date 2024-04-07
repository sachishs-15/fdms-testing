import os
import json
import random
from dotenv import load_dotenv

import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helpers.BaseRequest import get, post, put, delete

load_dotenv()

BACKEND_API_URL = os.getenv('BACKEND_API_URL', 'http://localhost:3000')

token=""
testOrderID = ""

def customerLogin(email, password, status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/customer/login"
    data = {
        "email": email,
        "password": password
    }

    schema = {
        'type': 'object',
        'properties': {
            'success': {'type': 'boolean'},
            'token': {'type': 'string'}
        },
        'required': ['success', 'token']
    }

    try:
        global token
        response = post(url, headers={}, data=data, status_code=status_code, schema=schema)
        if 'token' in response:
            token = response['token']
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False
    
    print(testMsg + "PASSED")
    return True

def customerSignup(email, password, name, phone, address, status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/customer/signup"
    data = {
        "email": email,
        "password": password,
        "name": name,
        "phone": phone,
        "address": address
    }
    
    schema = {
        'type': 'object',
        'properties': {
            'success': {'type': 'boolean'},
            'token': {'type': 'string'}
        },
        'required': ['success', 'token']
    }

    try:
        global token
        response = post(url, headers={}, data=data, status_code=status_code, schema=schema)
        if 'token' in response:
            token = response['token']
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False
    
    print(testMsg + "PASSED")
    return True

def customerInfo(status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/customer/info"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    schema = {
        'type': 'object',
        'properties': {
                'email': {'type': 'string'},
                'uid' : {'type': 'string'},
                'name': {'type': 'string'},
                'phone': {'type': 'string'},
                'address': {'type': 'string'}
        },
        'required': ['email', 'uid', 'name', 'phone', 'address']
    }

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False
    
    print(testMsg + "PASSED")
    return True

def customerEditInfo(name, phone, address, testMsg=""):
    url = f"{BACKEND_API_URL}/customer/edit"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    data = {
        "name": name,
        "phone": phone,
        "address": address
    }

    schema = {
        'type': 'object',
        'properties': {
            'success': {'type': 'boolean'}
        },
        'required': ['success']
    }

    try:
        response = put(url, headers=headers, data=data, status_code=200, schema=schema)
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False
    
    print(testMsg + "PASSED")
    return True

def customerOrders(status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/customer/orders"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    schema = {
        'type': 'array'
    }

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False
    
    print(testMsg + "PASSED")
    return True

def customerOrderByID(order_id, status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/customer/order/{order_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    schema = {
        'type': 'object',
        'properties': {
            'uid': {'type': 'string'},
            'restaurant': {'type': 'object'},
            'items': {'type': 'array'},
            'total': {'type': 'number'},
            'status': {'type': 'string'},
            'deliverer': {'type': 'object'},
            'isRestaurantRated': {'type': 'boolean'},
            'isDelivererRated': {'type': 'boolean'},
            'isCompleted' : {'type': 'boolean'}
        },
        'required': ['uid', 'restaurant', 'items', 'total', 'deliverer', 'isRestaurantRated', 'isDelivererRated', 'isCompleted']
    }

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False
    
    print(testMsg + "PASSED")
    return True

def customerNewOrder(restaurant_id, items, deliveryAddress, status_code=200, testMsg=""):
    print("New Order", restaurant_id, deliveryAddress)
    url = f"{BACKEND_API_URL}/customer/order"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    data = {
        "restaurant": restaurant_id,
        "items": items,
        "deliveryAddress": deliveryAddress
    }

    schema = {
        'type': 'object',
    }

    try:
        response = post(url, headers=headers, data=data, status_code=status_code, schema=schema)
        if(status_code == 200):
            global testOrderID
            testOrderID = response['uid']
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False
    
    print(testMsg + "PASSED")
    return True

def customerFavouriteRestaurants(status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/customer/favouriterestaurants"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    schema = {
        'type': 'array'
    }

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False
    
    print(testMsg + "PASSED")
    return True

def customerAddFavouriteRestaurant(restaurant_id, status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/customer/favouriterestaurant/{restaurant_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    schema = {
        'type': 'object',
        'properties': {
            'success': {'type': 'boolean'}
        },
        'required': ['success']
    }

    try:
        response = post(url, headers=headers, data={}, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False
    
    print(testMsg + "PASSED")
    return True

def customerRemoveFavouriteRestaurant(restaurant_id, status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/customer/favouriterestaurant/{restaurant_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    schema = {
        'type': 'object',
        'properties': {
            'success': {'type': 'boolean'}
        },
        'required': ['success']
    }

    try:
        response = delete(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False
    
    print(testMsg + "PASSED")
    return True
        

def customerGetRestaurants(status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/customer/restaurants"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    schema = {
        'type': 'array'
    }

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False
    
    print(testMsg + "PASSED")
    return True

def customerGetRestaurantByID(restaurant_id, status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/customer/restaurants/{restaurant_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    schema = {
        'type': 'object',
        'properties': {
            'uid': {'type': 'string'},
            'name': {'type': 'string'},
            'address': {'type': 'object'},
            'phone': {'type': 'string'},
            'rating': {'type': 'number'},
            'isFavourite': {'type': 'boolean'},
            'email' : {'type': 'string'},
            'menu': {'type': 'array'}
        },
        'required': ['uid', 'name', 'address', 'phone', 'rating', 'isFavourite', 'email', 'menu']
    }

def customerReviewRestaurant(restaurant_id, rating, comment, status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/reviews/restaurant/{restaurant_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    data = {
        "rating": rating,
        "comment": comment
    }
    
    schema = {
        'type': 'object',
        'properties': {
            'success': {'type': 'boolean'}
        },
    }

    try:
        response = post(url, headers=headers, data=data, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False
    
    print(testMsg + "PASSED")
    return True

def customerReviewDeliveryAgent(delivery_agent_id, rating, comment, status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/reviews/delivery_agent/{delivery_agent_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    data = {
        "rating": rating,
        "comment": comment
    }
    
    schema = {
        'type': 'object',
        'properties': {
            'success': {'type': 'boolean'}
        },
        'required': ['success']
    }

    try:
        response = post(url, headers=headers, data=data, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False
    
    print(testMsg + "PASSED")
    return True

def customerGetOffers(status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/customer/offers"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    schema = {
        'type': 'array'
    }
    
    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False
    
    print(testMsg + "PASSED")
    return True

def customerGetRecommendations(status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/customer/recommendations"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    schema = {
        'type': 'array'
    }

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False
    
    print(testMsg + "PASSED")
    return True

parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CREATION_DATA_PATH = os.path.join(parent_directory, 'creation_data', 'customers.json')

TEST_DATA_PATH = os.path.join(parent_directory, 'add_data', 'test_data', 'customers.json')
RESTAURANT_DATA_PATH = os.path.join(parent_directory, 'add_data', 'test_data', 'restaurants.json')
DISHES_DATA_PATH = os.path.join(parent_directory, 'add_data', 'test_data', 'dishes.json')

if __name__ == "__main__":
    count = 0

    customers = json.load(open(CREATION_DATA_PATH))
    customer = customers[random.randint(0, len(customers)-1)]
    print("SignUp", customer)
    if customerSignup(customer['email'], customer['password'], customer['name'], customer['phone'], customer['address'], status_code=201, testMsg="Successful Customer Signup: "):
        count += 1
    if customerSignup(customer['email'], customer['password'], customer['name'], customer['phone'], customer['address'], status_code=406, testMsg="Duplicate Customer Signup: "):
        count += 1

    customers = json.load(open(TEST_DATA_PATH))
    customer = customers[random.randint(0, len(customers)-1)]
    print("Login", customer)
    if customerLogin(customer['email'], customer['password'], status_code=200, testMsg="Successful Customer Login: "):
        count += 1
    if customerLogin(customer['email'], "wrongpassword", status_code=400, testMsg="Incorrect Customer Login: "):
        count += 1

    if customerInfo(status_code=200):
        count += 1

    restaurants = json.load(open(RESTAURANT_DATA_PATH))
    restaurant = restaurants[random.randint(0, len(restaurants)-1)]
    dishes = json.load(open(DISHES_DATA_PATH))
    itemList = []
    for dish in dishes:
        if dish['restaurant'] == restaurant['uid']:
            itemList.append({
                "dish": dish['uid'],
                "quantity": random.randint(1, 5)
            })

    if customerNewOrder(restaurant['uid'], itemList, customer["address"]["text"], status_code=200, testMsg="Customer New Order: "):
        count += 1
    if customerNewOrder("wrongid", itemList, customer["address"]["text"], status_code=406, testMsg="Customer Incorrect New Order: "):
        count += 1

    if customerOrders(status_code=200, testMsg="Customer get Orders: "):
        count += 1

    if customerOrderByID(testOrderID, status_code=200, testMsg="Customer get Order by ID: "):
        count += 1

    if customerGetRestaurants(status_code=200, testMsg="Customer get Restaurants: "):
        count += 1

    restaurant = restaurants[random.randint(0, len(restaurants)-1)]
    if customerGetRestaurantByID(restaurant['uid'], status_code=200, testMsg="Customer get Restaurant by ID: "):
        count += 1
    if customerGetRestaurantByID("wrongid", status_code=404, testMsg="Customer get Restaurant by Wrong ID: "):
        count += 1
    
    if customerFavouriteRestaurants(status_code=200, testMsg="Customer get Favourite Restaurants: "):
        count += 1

    if customerAddFavouriteRestaurant(restaurant['uid'], status_code=200, testMsg="Customer Add Favourite Restaurant: "):
        count += 1
    
    if customerRemoveFavouriteRestaurant(restaurant['uid'], status_code=200, testMsg="Customer Remove Favourite Restaurant: "):
        count += 1
    
    if customerGetRecommendations(status_code=200, testMsg="Customer get Recommended Restaurants: "):
        count += 1
    
    if customerGetOffers(status_code=200, testMsg="Customer get Offers: "):
        count += 1

    if customerReviewRestaurant(restaurant['uid'], 5, "Good Food", status_code=200, testMsg="Customer Review Restaurant: "):
        count += 1
    

    