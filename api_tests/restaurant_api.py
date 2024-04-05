import os
from dotenv import load_dotenv

import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helpers.BaseRequest import get, post, put, delete

load_dotenv()

BACKEND_API_URL = os.getenv('BACKEND_API_URL', 'http://localhost:3000')

token=None

def restaurantLogin(email, password, status_code=200):
    url = f"{BACKEND_API_URL}/restaurant/login"
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

def restaurantSignup(name, email, phone, password, address, timings, tags, image, status_code=200):
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
        'type': 'object',
        'properties': {
            'success': {'type': 'boolean'},
            'token': {'type': 'string'}
        },
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

def restaurantInfo(status_code=200):
    url = f"{BACKEND_API_URL}/restaurant/info"
    headers = {
        'Authorization': f"Bearer {token}"
    }
    schema = {
        'type': 'object',
        'properties': {
            'success': {'type': 'boolean'},
            'restaurant': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'email': {'type': 'string'},
                    'phone': {'type': 'string'},
                    'address': {'type': 'string'},
                    'timings': {'type': 'object'},
                    'tags': {'type': 'array'},
                    'image': {'type': 'string'},
                },
                'required': ['name', 'email', 'phone', 'address', 'timings', 'tags', 'image']
            }
        },
        'required': ['success', 'restaurant']
    }

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        return False
    
    return True

def restaurantEditInfo(name, email, phone, address, timings, tags, status_code=200):
    url = f"{BACKEND_API_URL}/restaurant/info"
    headers = {
        'Authorization': f"Bearer {token}"
    }

    data = {
        "name": name,
        "email": email,
        "phone": phone,
        "address": address,
        "timings": timings,
        "tags": tags,
    }

    schema = {
        'type': 'object',
        'properties': {
            'success': {'type': 'boolean'},
            'restaurant': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'email': {'type': 'string'},
                    'phone': {'type': 'string'},
                    'address': {'type': 'string'},
                    'timings': {'type': 'object'},
                    'tags': {'type': 'array'},
                    'image': {'type': 'string'},
                },
                'required': []
            }
        },
        'required': ['success', 'restaurant']
    }

    try:
        response = put(url, headers=headers, data=data, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        return False
    
    return True

#IMAGE UPLOAD

def restaurantOrders(status_code=200):
    url = f"{BACKEND_API_URL}/restaurant/orders"

    headers = {
        'Authorization': f"Bearer {token}"
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

def restaurantOrderByID(order_id, status_code=200):
    url = f"{BACKEND_API_URL}/restaurant/orders/{order_id}"

    headers = {
        'Authorization': f"Bearer {token}"
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
            'isCompleted' : {'type': 'boolean'}
        },
        'required': ['uid', 'restaurant', 'items', 'total', 'status', 'delivery_agent', 'isCompleted']
    }

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        return False
    
    return True

def restaurantMenu(status_code=200):
    url = f"{BACKEND_API_URL}/restaurant/menu"

    headers = {
        'Authorization': f"Bearer {token}"
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

def restaurantAddFoodItem(name, price, status_code=200):
    url = f"{BACKEND_API_URL}/restaurant/menu"

    headers = {
        'Authorization': f"Bearer {token}"
    }

    data = {
        'name': name,
        'price': price
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

def restaurantFoodItem(uid, status_code=200):
    url = f"{BACKEND_API_URL}/restaurant/menu/{uid}"

    headers = {
        'Authorization': f"Bearer {token}"
    }

    schema = {
        'type': 'object',
        'properties': {
            'name': {'type': 'string'},
            'price': {'type': 'number'},
            'isAvailable': {'type': 'boolean'}
        },
        'required': ['name', 'price', 'isAvailable']
    }

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        return False
    
    return True

def restaurantRemoveFoodItem(uid, status_code=200):
    url = f"{BACKEND_API_URL}/restaurant/menu/{uid}"

    headers = {
        'Authorization': f"Bearer {token}"
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
    
    return True

def restaurantUpdateFoodItem(uid, name, price, isAvailable, status_code=200):
    url = f"{BACKEND_API_URL}/restaurant/menu/{uid}"

    headers = {
        'Authorization': f"Bearer {token}"
    }

    data = {
        'name': name,
        'price': price,
        'isAvailable': isAvailable
    }

    schema = {
        'type': 'object',
        'properties': {
            'success': {'type': 'boolean'}
        },
        'required': ['success']
    }

    try:
        response = put(url, headers=headers, data=data, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        return False
    
    return True

# FOOD ITEM IMAGE

def restaurantReviews(status_code=200):
    url = f"{BACKEND_API_URL}/restaurant/reviews"

    headers = {
        'Authorization': f"Bearer {token}"
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



