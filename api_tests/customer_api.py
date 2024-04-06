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

def customerLogin(email, password, status_code=200):
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
        return False
    
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

def customerInfo(status_code=200):
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
        return False
    
    return True

def customerEditInfo(name, phone, address):
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
        return False
    
    return True

def customerOrders(status_code=200):
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
        return False
    
    return True

def customerOrderByID(order_id, status_code=200):
    url = f"{BACKEND_API_URL}/customer/orders/{order_id}"
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
            'delivery_agent': {'type': 'object'},
            'isRestaurantRated': {'type': 'boolean'},
            'isDelivererRated': {'type': 'boolean'},
            'isCompleted' : {'type': 'boolean'}
        },
        'required': ['uid', 'restaurant', 'items', 'total', 'status', 'delivery_agent', 'isRestaurantRated', 'isDelivererRated', 'isCompleted']
    }

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        return False
    
    return True

def customerFavouriteRestaurants(status_code=200):
    url = f"{BACKEND_API_URL}/customer/favourites"
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
        return False
    
    return True

def customerAddFavouriteRestaurant(restaurant_id, status_code=200):
    url = f"{BACKEND_API_URL}/customer/favourites/{restaurant_id}"
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
        return False
    
    return True

def customerRemoveFavouriteRestaurant(restaurant_id, status_code=200):
    url = f"{BACKEND_API_URL}/customer/favourites/{restaurant_id}"
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
        return False
        

def customerGetRestaurants(status_code=200):
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
        return False
    
    return True

def customerGetRestaurantByID(restaurant_id):
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

def customerReviewRestaurant(restaurant_id, rating, comment, status_code=200):
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
        return False
    
    return True

def customerReviewDeliveryAgent(delivery_agent_id, rating, comment, status_code=200):
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
        return False
    
    return True

def customerGetOffers(status_code=200):
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
        return False
    
    return True

def customergetRecommendations(status_code=200):
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
        return False
    
    return True

parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CREATION_DATA_PATH = os.path.join(parent_directory, 'creation_data', 'customers.json')

if __name__ == "__main__":
    count = 0

    customers = json.load(open(CREATION_DATA_PATH))
    customer = customers[random.randint(0, len(customers)-1)]
    if customerSignup(customer['email'], customer['password'], customer['name'], customer['phone'], customer['address'], status_code=201, testMsg="Successful Customer Signup test: "):
        count += 1
    if customerSignup(customer['email'], customer['password'], customer['name'], customer['phone'], customer['address'], status_code=406, testMsg="Duplicate Customer Signup test: "):
        count += 1

    