import os
from dotenv import load_dotenv

import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helpers.BaseRequest import get, post, put, delete

load_dotenv()

BACKEND_API_URL = os.getenv('BACKEND_API_URL', 'http://localhost:3000')

token=None

def managementLogin(email, password, status_code=200):
    url = f"{BACKEND_API_URL}/management/login"
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

def managementInfo(status_code=200):
    url = f"{BACKEND_API_URL}/management/info"
    headers = {
        'Authorization': f'Bearer {token}'
    }

    schema = {
        'type' : 'object',
        'properties': {
            'email': {'type': 'string'},
            'name': {'type': 'string'},
            'phone': {'type': 'string'},
            'uid': {'type': 'string'},

        },
        'required': ['email', 'name', 'phone', 'uid']
    }

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        return False
    
    return True

def managementEditInfo(name, phone, status_code=200):
    url = f"{BACKEND_API_URL}/management/edit-info"
    headers = {
        'Authorization': f'Bearer {token}'
    }
    data = {
        'name': name,
        'phone': phone
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

def managementCustomers(status_code=200):
    url = f"{BACKEND_API_URL}/management/customers"
    headers = {
        'Authorization': f'Bearer {token}'
    }

    schema = {
        'type' : 'array',
    }

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        return False
    
    return True

def managementDeliverers(status_code=200):
    url = f"{BACKEND_API_URL}/management/deliverers"
    headers = {
        'Authorization': f'Bearer {token}'
    }

    schema = {
        'type' : 'array',
    }

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        return False
    
    return True

def managementRestaurants(status_code=200):
    url = f"{BACKEND_API_URL}/management/restaurants"
    headers = {
        'Authorization': f'Bearer {token}'
    }

    schema = {
        'type' : 'array',
    }

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        return False
    
    return True

def managementCustomerById(uid, status_code=200):
    url = f"{BACKEND_API_URL}/management/customer/{uid}"
    headers = {
        'Authorization': f'Bearer {token}'
    }

    schema = {
        'type' : 'object',
        'properties': {
            'email': {'type': 'string'},
            'name': {'type': 'string'},
            'phone': {'type': 'string'},
            'address': {'type': 'string'},
        },
        'required': ['email', 'name', 'phone', 'address']
    }

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        return False
    
    return True

def managementDelivererById(uid, status_code=200):
    url = f"{BACKEND_API_URL}/management/deliverer/{uid}"
    headers = {
        'Authorization': f'Bearer {token}'
    }

    schema = {
        'type' : 'object',
        'properties': {
            'email': {'type': 'string'},
            'name': {'type': 'string'},
            'phone': {'type': 'string'},
            'reviews': {'type': 'array'},
            'pendingMoney': {'type': 'number'},
        },
        'required': ['email', 'name', 'phone', 'reviews', 'pendingMoney']
    }

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        return False
    
    return True

def managementRestaurantById(uid, status_code=200):
    url = f"{BACKEND_API_URL}/management/restaurant/{uid}"
    headers = {
        'Authorization': f'Bearer {token}'
    }

    schema = {
        'type' : 'object',
        'properties': {
            'name': {'type': 'string'},
            'email': {'type': 'string'},
            'phone': {'type': 'string'},
            'address': {'type': 'string'},
            'timings': {'type': 'object'},
            'tags': {'type': 'array'},
        },
        'required': ['name', 'email', 'phone', 'address', 'timings', 'tags']
    }

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        return False
    
    return True

def managementOrdersbyCustomer(uid, status_code=200):
    url = f"{BACKEND_API_URL}/management/orders/customer/{uid}"
    headers = {
        'Authorization': f'Bearer {token}'
    }

    schema = {
        'type' : 'array',
    }

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        return False
    
    return True

def managementOrdersbyDeliverer(uid, status_code=200):
    url = f"{BACKEND_API_URL}/management/orders/deliverer/{uid}"
    headers = {
        'Authorization': f'Bearer {token}'
    }

    schema = {
        'type' : 'array',
    }

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        return False
    
    return True

def managementOrdersbyRestaurant(uid, status_code=200):
    url = f"{BACKEND_API_URL}/management/orders/restaurant/{uid}"
    headers = {
        'Authorization': f'Bearer {token}'
    }

    schema = {
        'type' : 'array',
    }

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        return False
    
    return True

def managementMarkPaid(uid, status_code=200):
    url = f"{BACKEND_API_URL}/management/markpaid/deliverer/{uid}"
    headers = {
        'Authorization': f'Bearer {token}'
    }

    schema = {
        'type' : 'object',
        'properties': {
            'success': {'type': 'boolean'}
        },
        'required': ['success']
    }

    try:
        response = put(url, headers=headers, data={}, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        return False
    
    return True

def managementMarkPaidRes(uid, status_code=200):
    url = f"{BACKEND_API_URL}/management/markpaid/restaurant/{uid}"
    headers = {
        'Authorization': f'Bearer {token}'
    }

    schema = {
        'type' : 'object',
        'properties': {
            'success': {'type': 'boolean'}
        },
        'required': ['success']
    }

    try:
        response = put(url, headers=headers, data={}, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        return False
    
    return True

def managementOffers(status_code=200):
    url = f"{BACKEND_API_URL}/management/offers"
    headers = {
        'Authorization': f'Bearer {token}'
    }

    schema = {
        'type' : 'array',
    }

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        return False
    
    return True

def managementCreateOffer(code, discount, status_code=200):
    url = f"{BACKEND_API_URL}/management/offer"
    headers = {
        'Authorization': f'Bearer {token}'
    }

    data = {
        'code': code,
        'discount': discount
    }

    schema = {
        'type' : 'object',
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

def managementDeleteOffer(code, status_code=200):
    url = f"{BACKEND_API_URL}/management/offer/{code}"
    headers = {
        'Authorization': f'Bearer {token}'
    }

    schema = {
        'type' : 'object',
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


        