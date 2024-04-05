import os
from dotenv import load_dotenv

import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helpers.BaseRequest import get, post, put, delete

load_dotenv()

BACKEND_API_URL = os.getenv('BACKEND_API_URL', 'http://localhost:3000')

token=None

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

def customerSignup(email, password, name, phone, address, status_code=200):
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


if __name__ == "__main__":
    print("Running customer API tests")
    print("Testing customerLogin")
    print(customerLogin("Jessy_Crona@yahoo.com", "test123"))
    print(token)
    print("Testing customerInfo")
    print(customerInfo())
