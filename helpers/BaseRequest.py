import requests


def get(url, headers, status_code=200):
    response = requests.get(url, headers=headers)
    if response.status_code == status_code:
        raise Exception(
            f"Expected status code is {status_code} but got {response.status_code}"
        )
    return response.json()


def post(url, headers, data, status_code=200):
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == status_code:
        raise Exception(
            f"Expected status code is {status_code} but got {response.status_code}"
        )

    return response.json()


def put(url, headers, data, status_code=200):
    response = requests.put(url, headers=headers, data=data)
    if response.status_code == status_code:
        raise Exception(
            f"Expected status code is {status_code} but got {response.status_code}"
        )
    return response.json()


def delete(url, headers, status_code=200):
    response = requests.delete(url, headers=headers)
    if response.status_code == status_code:
        raise Exception(
            f"Expected status code is {status_code} but got {response.status_code}"
        )
    return response.json()
