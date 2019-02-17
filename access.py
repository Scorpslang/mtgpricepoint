from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__, template_folder='template')


def read_json(file):
    with open(file) as f:
        data = json.load(f)
    return data


def generate_bearer(data):
    headers = {"Authorization": 'application/x-www-form-urlencoded'}
    data = 'grant_type=client_credentials&client_id=' + get_public_key(data) + '&client_secret=' + get_private_key(data)
    response = requests.post('https://api.tcgplayer.com/token', headers=headers, data=data)
    return response


def get_token(data):
    return data["access_token"]


def get_private_key(data):
    return data["private_key"]


def get_public_key(data):
    return data["public_key"]


def get_catagories(token):
    headers = {
        'Accept': 'application/json',
        'Authorization': 'bearer ' + token,
    }
    response = requests.get('http://api.tcgplayer.com/v1.19.0/catalog/categories', headers=headers)
    return response.text


def get_price(id, token):
    headers = {
        'Accept': 'application/json',
        'Authorization': 'bearer ' + token,
    }
    import requests

    url = "http://api.tcgplayer.com/v1.19.0/pricing/product/"+id

    response = requests.request("GET", url, headers=headers)

    return response.json()

def get_all_mtg(token):
    headers = {
        'Accept': 'application/json',
        'Authorization': 'bearer ' + token,
    }
    url = "http://api.tcgplayer.com/v1.20.0/catalog/products"

    querystring = {"categoryId": "1", "groupId": 2366, "limit": "1000"}

    response = requests.request("GET", url, params=querystring, headers=headers)

    return response.text


def get_all_media(token):
    headers = {
        'Accept': 'application/json',
        'Authorization': 'bearer ' + token,
    }

    url = "http://api.tcgplayer.com/v1.19.0/catalog/categories/2336/media"
    response = requests.request("GET", url, headers=headers)

    print(response.text)


def get_product_info(product, token):
    headers = {
        'Accept': 'application/json',
        'Authorization': 'bearer ' + token,
    }
    url = "http://api.tcgplayer.com/v1.19.0/catalog/products/" + product

    response = requests.request("GET", url, headers=headers)

    print(response.text)


def get_products(token):
    headers = {
        'Accept': 'application/json',
        'Authorization': 'bearer ' + token,
    }
    url = "http://api.tcgplayer.com/v1.19.0/catalog/products"
    response = requests.request("GET", url, headers=headers)
    print(response.text)
