import os
from dotenv import load_dotenv

import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helpers.BaseRequest import get, post, put, delete

load_dotenv()

BACKEND_API_URL = os.getenv('BACKEND_API_URL', 'http://localhost:3000')

token=None

def deliveryAgentLogin(email, password, status_code=200):
    url = f"{BACKEND_API_URL}/delivery-agent/login"
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

def deliveryAgentSignup(email, password, name, phone, status_code=200):
    url = f"{BACKEND_API_URL}/delivery-agent/signup"
    data = {
        "email": email,
        "password": password,
        "name": name,
        "phone": phone
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

def deliveryAgentInfo(status_code=200):
    url = f"{BACKEND_API_URL}/delivery-agent/info"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    schema = {
        'type': 'object',
        'properties': {
            'success': {'type': 'boolean'},
            'data': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'email': {'type': 'string'},
                    'phone': {'type': 'string'},
                    'workingStatus': {'type': 'number'},
                    'location' : {'type': 'object'},
                },
                'required': ['name', 'email', 'phone', 'workingStatus', 'location']
            }
        },
    }

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        return False
    
    return True

def deliveryAgentEditInfo(name, phone, status_code=200):
    url = f"{BACKEND_API_URL}/delivery-agent/info"
    headers = {
        'Authorization': f"Bearer {token}"
    }

    data = {
        "name": name,
        "phone": phone
    }

    schema = {
        'type': 'object',
        'properties': {
            'success': {'type': 'boolean'},
        },
        'required': ['success']
    }

    try:
        response = put(url, headers=headers, data=data, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        return False
    
    return True

def deliveryAgentOrders(status_code=200):
    url = f"{BACKEND_API_URL}/delivery-agent/orders"
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

def deliveryAgentOrderByID(uid, status_code=200):
    url = f"{BACKEND_API_URL}/delivery-agent/orders/{uid}"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    schema = {
        'type': 'object',
        'properties': {
            'uid': {'type': 'string'},
            'restaurant': {'type': 'object'},
            'delivery_agent': {'type': 'object'},
            'items': {'type': 'array'},
            'total': {'type': 'number'},
            'status': {'type': 'string'},
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

def deliveryAgentFinishOrder(uid, otp, status_code=200):
    url = f"{BACKEND_API_URL}/delivery-agent/orders/{uid}"
    headers = {
        'Authorization': f"Bearer {token}"
    }

    data = {
        "otp": otp
    }

    schema = {
        'type': 'object',
        'properties': {
            'success': {'type': 'boolean'},
        },
        'required': ['success']
    }

    try:
        response = put(url, headers=headers, data=data, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        return False
    
    return True

def deliveryAgentUpdateLocation(location, status_code=200):
    url = f"{BACKEND_API_URL}/delivery-agent/location"
    headers = {
        'Authorization': f"Bearer {token}"
    }
    
    data = {
        "location": location
    }

    schema = {
        'type': 'object',
        'properties': {
            'success': {'type': 'boolean'},
        },
        'required': ['success']
    }

    try:
        response = put(url, headers=headers, data=data, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        return False
    
    return True

def deliveryAgentPauseWorking(status_code=200):
    url = f"{BACKEND_API_URL}/delivery-agent/working"
    headers = {
        'Authorization': f"Bearer {token}"
    }

    schema = {
        'type': 'object',
        'properties': {
            'success': {'type': 'boolean'},
        },
        'required': ['success']
    }

    try:
        response = put(url, headers=headers, data={}, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        return False
    
    return True

def deliveryAgentReviews(status_code=200):
    url = f"{BACKEND_API_URL}/delivery-agent/reviews"
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



