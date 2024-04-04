import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

BACKEND_API_URL = os.getenv('BACKEND_API_URL', 'http://localhost:3000')

def customerLogin(email, password):
    url = f"{BACKEND_API_URL}/customer/login"
    data = {
        "email": email,
        "password": password
    }
    response = requests.post(url, json=data)
    ret = json.loads(response.text)
    return (ret, response.status_code)

def customerSignup(email, password, name, phone, address):
    url = f"{BACKEND_API_URL}/customer/signup"
    data = {
        "email": email,
        "password": password,
        "name": name,
        "phone": phone,
        "address": address
    }
    response = requests.post(url, json=data)
    ret = json.loads(response.text)
    return (ret, response.status_code)

def customerInfo(token):
    url = f"{BACKEND_API_URL}/customer/info"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    ret = json.loads(response.text)
    return (ret, response.status_code)

def customerEditInfo(token, name, phone, address):
    url = f"{BACKEND_API_URL}/customer/edit"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    data = {
        "name": name,
        "phone": phone,
        "address": address
    }
    response = requests.put(url, headers=headers, json=data)
    ret = json.loads(response.text)
    return (ret, response.status_code)

def customerOrders(token):
    url = f"{BACKEND_API_URL}/customer/orders"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    ret = json.loads(response.text)
    return (ret, response.status_code)

def customerOrderByID(token, order_id):
    url = f"{BACKEND_API_URL}/customer/orders/{order_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    ret = json.loads(response.text)
    return (ret, response.status_code)

def customerFavouriteRestaurants(token):
    url = f"{BACKEND_API_URL}/customer/favourites"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    ret = json.loads(response.text)
    return (ret, response.status_code)

def customerAddFavouriteRestaurant(token, restaurant_id):
    url = f"{BACKEND_API_URL}/customer/favourites/{restaurant_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.post(url, headers=headers)
    ret = json.loads(response.text)
    return (ret, response.status_code)

def customerGetRestaurants(token):
    url = f"{BACKEND_API_URL}/customer/restaurants"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    ret = json.loads(response.text)
    return (ret, response.status_code)

def customerGetRestaurantByID(token, restaurant_id):
    url = f"{BACKEND_API_URL}/customer/restaurants/{restaurant_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    ret = json.loads(response.text)
    return (ret, response.status_code)

def customerReviewRestaurant(token, restaurant_id, rating, comment):
    url = f"{BACKEND_API_URL}/reviews/restaurant/{restaurant_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    data = {
        "rating": rating,
        "comment": comment
    }
    response = requests.post(url, headers=headers, json=data)
    ret = json.loads(response.text)
    return (ret, response.status_code)

def customerReviewDeliveryAgent(token, delivery_agent_id, rating, comment):
    url = f"{BACKEND_API_URL}/reviews/delivery_agent/{delivery_agent_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    data = {
        "rating": rating,
        "comment": comment
    }
    response = requests.post(url, headers=headers, json=data)
    ret = json.loads(response.text)
    return (ret, response.status_code)

def customerGetOffers(token):
    url = f"{BACKEND_API_URL}/customer/offers"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    ret = json.loads(response.text)
    return (ret, response.status_code)

def customergetRecommendations(token):
    url = f"{BACKEND_API_URL}/customer/recommendations"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    ret = json.loads(response.text)
    return (ret, response.status_code)




