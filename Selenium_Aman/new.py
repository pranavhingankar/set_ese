# import requests


# def fetch_data(url):
#     response = requests.get(url)
#     data = response.json()
#     return data


# api_url = input("Enter the API URL: ")
# data = fetch_data(api_url)
# print(data)


import requests
from urllib.parse import urlparse


def fetch_data(url):
    parsed_url = urlparse(url)
    if parsed_url.scheme and parsed_url.netloc:
        response = requests.get(url)
        data = response.json()
        return data
    else:
        print("Invalid URL!")


api_url = input("Enter the API URL: ")
data = fetch_data(api_url)
if data:
    print(data)
