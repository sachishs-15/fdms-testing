import os
import random
import json
from dotenv import load_dotenv

import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helpers.BaseRequest import get, post, put, delete

load_dotenv()

BACKEND_API_URL = os.getenv("BACKEND_API_URL", "http://localhost:3000")

token = ""
testIDs = {}


def managementLogin(email, password, status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/management/login"
    data = {"email": email, "password": password}

    schema = {
        "type": "object",
        "properties": {"success": {"type": "boolean"}, "token": {"type": "string"}},
        "required": ["success", "token"],
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


def managementInfo(status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/management/info"
    headers = {"Authorization": f"Bearer {token}"}

    schema = {
        "type": "object",
        "properties": {
            "email": {"type": "string"},
            "name": {"type": "string"},
            "phone": {"type": "string"},
            "uid": {"type": "string"},
        },
        "required": ["email", "name", "phone", "uid"],
    }

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False

    print(testMsg + "PASSED")
    return True


def managementEditInfo(name, phone, status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/management/info"
    headers = {"Authorization": f"Bearer {token}"}
    data = {"name": name, "phone": phone}

    schema = {
        "type": "object",
        "properties": {"success": {"type": "boolean"}},
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


def managementCustomers(status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/management/customers"
    headers = {"Authorization": f"Bearer {token}"}

    schema = {
        "type": "array",
    }

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
        if len(response) > 0:
            testIDs["customer"] = response[0]["uid"]
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False

    print(testMsg + "PASSED")
    return True


def managementDeliverers(status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/management/deliverers"
    headers = {"Authorization": f"Bearer {token}"}

    schema = {
        "type": "array",
    }

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
        if len(response) > 0:
            testIDs["deliverer"] = response[0]["uid"]
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False

    print(testMsg + "PASSED")
    return True


def managementRestaurants(status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/management/restaurants"
    headers = {"Authorization": f"Bearer {token}"}

    schema = {
        "type": "array",
    }

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
        if len(response) > 0:
            testIDs["restaurant"] = response[0]["uid"]
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False

    print(testMsg + "PASSED")
    return True


def managementCustomerById(uid, status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/management/customer/{uid}"
    headers = {"Authorization": f"Bearer {token}"}

    schema = {
        "type": "object",
        "properties": {
            "email": {"type": "string"},
            "name": {"type": "string"},
            "phone": {"type": "string"},
            "address": {"type": "string"},
        },
        "required": ["email", "name", "phone", "address"],
    }

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False

    print(testMsg + "PASSED")
    return True


def managementDelivererById(uid, status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/management/deliverer/{uid}"
    headers = {"Authorization": f"Bearer {token}"}

    schema = {
        "type": "object",
        "properties": {
            "email": {"type": "string"},
            "name": {"type": "string"},
            "phone": {"type": "string"},
            "reviews": {"type": "array"},
            "pendingMoney": {"type": "number"},
        },
        "required": ["email", "name", "phone", "reviews", "pendingMoney"],
    }

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False

    print(testMsg + "PASSED")
    return True


def managementRestaurantById(uid, status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/management/restaurant/{uid}"
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


def managementOrdersbyCustomer(uid, status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/management/orders/customer/{uid}"
    headers = {"Authorization": f"Bearer {token}"}

    schema = {
        "type": "array",
    }

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False

    print(testMsg + "PASSED")
    return True


def managementOrdersbyDeliverer(uid, status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/management/orders/deliverer/{uid}"
    headers = {"Authorization": f"Bearer {token}"}

    schema = {
        "type": "array",
    }

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False

    print(testMsg + "PASSED")
    return True


def managementOrdersbyRestaurant(uid, status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/management/orders/restaurant/{uid}"
    headers = {"Authorization": f"Bearer {token}"}

    schema = {
        "type": "array",
    }

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False

    print(testMsg + "PASSED")
    return True


def managementMarkPaid(uid, status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/management/markpaid/deliverer/{uid}"
    headers = {"Authorization": f"Bearer {token}"}

    schema = {
        "type": "object",
        "properties": {"success": {"type": "boolean"}},
        "required": ["success"],
    }

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


def managementMarkPaidRes(uid, status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/management/markpaid/restaurant/{uid}"
    headers = {"Authorization": f"Bearer {token}"}

    schema = {
        "type": "object",
        "properties": {"success": {"type": "boolean"}},
        "required": ["success"],
    }

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


def managementOffers(status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/management/offers"
    headers = {"Authorization": f"Bearer {token}"}

    schema = {
        "type": "array",
    }

    try:
        response = get(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False

    print(testMsg + "PASSED")
    return True


def managementCreateOffer(code, discount, status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/management/offer"
    headers = {"Authorization": f"Bearer {token}"}

    data = {"code": code, "discount": discount}

    schema = {
        "type": "object",
        "properties": {"success": {"type": "boolean"}},
        "required": ["success"],
    }

    try:
        response = post(
            url, headers=headers, data=data, status_code=status_code, schema=schema
        )
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False

    print(testMsg + "PASSED")
    return True


def managementDeleteOffer(code, status_code=200, testMsg=""):
    url = f"{BACKEND_API_URL}/management/offer/{code}"
    headers = {"Authorization": f"Bearer {token}"}

    schema = {
        "type": "object",
        "properties": {"success": {"type": "boolean"}},
        "required": ["success"],
    }

    try:
        response = delete(url, headers=headers, status_code=status_code, schema=schema)
    except Exception as e:
        print(e)
        print(testMsg + "FAILED")
        return False

    print(testMsg + "PASSED")
    return True


parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEST_DATA_PATH = os.path.join(
    parent_directory, "add_data", "test_data", "management.json"
)


def run_management_tests():
    tests_conducted = 0
    count = 0

    managements = json.load(open(TEST_DATA_PATH))
    management = random.choice(managements)

    print("Running Management Tests...")

    tests_conducted += 1
    if managementLogin(
        management["email"],
        management["password"],
        status_code=200,
        testMsg="Management Login Test ",
    ):
        count += 1

    tests_conducted += 1
    if managementInfo(status_code=200, testMsg="Management Info Test "):
        count += 1

    tests_conducted += 1
    if managementCustomers(status_code=200, testMsg="Management Customers Test "):
        count += 1

    tests_conducted += 1
    if managementDeliverers(status_code=200, testMsg="Management Deliverers Test "):
        count += 1

    tests_conducted += 1
    if managementRestaurants(status_code=200, testMsg="Management Restaurants Test "):
        count += 1

    if "customer" in testIDs:
        tests_conducted += 1
        if managementCustomerById(
            testIDs["customer"],
            status_code=200,
            testMsg="Management Customer By ID Test ",
        ):
            count += 1

        tests_conducted += 1
        if managementOrdersbyCustomer(
            testIDs["customer"],
            status_code=200,
            testMsg="Management Orders By Customer Test ",
        ):
            count += 1

    if "deliverer" in testIDs:
        tests_conducted += 1
        if managementDelivererById(
            testIDs["deliverer"],
            status_code=200,
            testMsg="Management Deliverer By ID Test ",
        ):
            count += 1

        tests_conducted += 1
        if managementOrdersbyDeliverer(
            testIDs["deliverer"],
            status_code=200,
            testMsg="Management Orders By Deliverer Test ",
        ):
            count += 1

        tests_conducted += 1
        if managementMarkPaid(
            testIDs["deliverer"], status_code=200, testMsg="Management Mark Paid Test "
        ):
            count += 1

    if "restaurant" in testIDs:

        tests_conducted += 1
        if managementRestaurantById(
            testIDs["restaurant"],
            status_code=200,
            testMsg="Management Restaurant By ID Test ",
        ):
            count += 1

        tests_conducted += 1
        if managementOrdersbyRestaurant(
            testIDs["restaurant"],
            status_code=200,
            testMsg="Management Orders By Restaurant Test ",
        ):
            count += 1

        tests_conducted += 1
        if managementMarkPaidRes(
            testIDs["restaurant"],
            status_code=200,
            testMsg="Management Mark Paid Restaurant Test ",
        ):
            count += 1

    tests_conducted += 1
    if managementOffers(status_code=200, testMsg="Management Offers Test "):
        count += 1

    tests_conducted += 1
    if managementCreateOffer(
        "TESTOFFER", 10, status_code=200, testMsg="Management Create Offer Test "
    ):
        count += 1

    tests_conducted += 1
    if managementDeleteOffer(
        "TESTOFFER", status_code=200, testMsg="Management Delete Offer Test "
    ):
        count += 1

    print(f"{count}/{tests_conducted} tests passed.\n")


if __name__ == "__main__":

    run_management_tests()
