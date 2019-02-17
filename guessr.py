from flask import Flask, render_template, request
import requests, json, access, random

app = Flask(__name__)


@app.route("/")
def home():
    card = generate_random_card()
    name = card_name(card)
    price = market_price(card)
    return render_template('front.html')

def card_name(card):
    return str(card['name'])

def card_image(card):
    return str(card['imageUrl'])

def card_productId(card):
    return str(card['productId'])

def guess(price):
    user = float(input("Guess how much this card costs: "))
    sprice = float(price.strip('$'))
    difference = user - sprice
    print("The market price was "+price+".")
    if difference < 0:
        difference *= -1
        print("You were $"+str(difference)+" below the market price")
    elif difference > 0:
        print("You were $" + str(difference) + " above the market price")
    else:
        print("You guessed that amount! Good job!")



def get_dict():
    return access.read_json('rna.json')


def generate_random_card():
    dict = get_dict()
    results = dict["results"]
    n = random.randint(0, len(results) - 1)
    return results[n]

def market_price(card):
    data = access.read_json('tcg.json')
    token = access.get_token(data)
    prices = access.get_price(card_productId(card), token)
    results = prices["results"]
    non_foil = results[1]
    return '$'+str(non_foil['marketPrice'])

if __name__ == "__main__":
    #app.run(debug=True)
    card = generate_random_card()
    name = card_name(card)
    price = market_price(card)
    print(name)
    guess(price)
