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

def deliveryAgentLogin(email, password, status_code=200, testMsg=""):
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
        print(testMsg + "FAILED")
        return False
    
    print(testMsg + "PASSED")
    return True

def deliveryAgentSignup(email, password, name, phone, status_code=200, testMsg=""):
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
        print(testMsg + "FAILED")
        return False
    
    print(testMsg + "PASSED")
    return True

def deliveryAgentInfo(status_code=200, testMsg=""):
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
        print(testMsg + "FAILED")
        return False
    
    print(testMsg + "PASSED")
    return True

def deliveryAgentEditInfo(name, phone, status_code=200, testMsg=""):
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
        print(testMsg + "FAILED")
        return False
    
    print(testMsg + "PASSED")
    return True

def deliveryAgentOrders(status_code=200, testMsg=""):
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
        print(testMsg + "FAILED")
        return False
    
    print(testMsg + "PASSED")
    return True

def deliveryAgentOrderByID(uid, status_code=200, testMsg=""):
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
        print(testMsg + "FAILED")
        return False
    
    print(testMsg + "PASSED")
    return True

def deliveryAgentFinishOrder(uid, otp, status_code=200, testMsg=""):
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
        print(testMsg + "FAILED")
        return False
    
    print(testMsg + "PASSED")
    return True

def deliveryAgentUpdateLocation(location, status_code=200, testMsg=""):
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
        print(testMsg + "FAILED")
        return False
    
    print(testMsg + "PASSED")
    return True

def deliveryAgentPauseWorking(status_code=200, testMsg=""):
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
        print(testMsg + "FAILED")
        return False
    
    print(testMsg + "PASSED")
    return True

def deliveryAgentReviews(status_code=200, testMsg=""):
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
        print(testMsg + "FAILED")
        return False
    
    print(testMsg + "PASSED")
    return True

parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CREATION_DATA_PATH = os.path.join(parent_directory, 'creation_data', 'delivery-agents.json')

if __name__ == "__main__":
    count = 0

    deliveryAgents = json.load(open(CREATION_DATA_PATH))
    deliveryAgent = deliveryAgents[random.randint(0, len(deliveryAgents)-1)]
    if deliveryAgentSignup(deliveryAgent['email'], deliveryAgent['password'], deliveryAgent['name'], deliveryAgent['phone'], status_code=201, testMsg="Successful Agent Signup test: "):
        count += 1
    if deliveryAgentSignup(deliveryAgent['email'], deliveryAgent['password'], deliveryAgent['name'], deliveryAgent['phone'], status_code=406, testMsg="Duplicate Agent Signup test: "):
        count += 1

    if deliveryAgentInfo(status_code=200, testMsg="Agent Info test: "):
        count += 1
    
    if deliveryAgentPauseWorking(status_code=200, testMsg="Agent Pause Working test: "):
        count += 1
        

