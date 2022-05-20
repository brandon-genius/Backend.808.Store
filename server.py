

from unittest import mock
from flask import Flask, request
import json
from mock_data import mock_catalog
from config import db

app = Flask('server')


@app.route("/home")
def home():
    return "sup"


home()


@app.route("/")
def root():
    return "Welcome to the store"


###############################################################
###############################################################
########################  API CATELOG  ########################

@app.route("/api/about", methods=['post'])
def about():
    me = {
        "first_name": "Brandon",
        "last_name": "Britt",
        "age": 30,
        "address": {
            "num": 1200,
            "street": "Queen Emma",
            "city": "Honolulu"
        }
    }
    return json.dumps(me) #parse into json, then return

@app.route("/api/catalog")
def get_catalog():
    cursor = db.products.find({})
    all_products = []

    for prod in cursor:
        prod["_id"] = str(prod["_id"])
        all_products.append(prod)

    return json.dumps(all_products)



@app.route("/api/catalog", methods=["post"])
def save_product():
    product = request.get_json()
    db.products.insert_one(product)

    print("Product saved")
    print(product)

    product["_id"] = str(product["_id"])

    return json.dumps(product)



#/api/catalog/cheapest
#returns the cheapest prod in cat

@app.route("/api/catalog/cheapest")    
def get_cheapest():
    #get data
    cursor = db.products.find({})
    solution = cursor[0]
    for prod in cursor:
        if prod["price"] < solution["price"]:
            solution = prod
    solution["_id"] = str(solution["_id"])
    return json.dumps(solution)


@app.route("/api/catalog/total")
def get_total():
    #get data
    cursor = db.products.find({})
    total = 0
    for prod in mock_catalog:
        total += prod["price"]

    return json.dumps(total)



#find a product based on the unique id
@app.route("/api/products/<id>")
def find_product(id):
    for prod in mock_catalog:
        if id == prod["_id"]:
            return json.dumps(prod)


@app.route("/api/products/categories")
def get_categories():
    categories = []
    for prod in mock_catalog:
        cat = prod["category"]
        if cat not in categories:
            categories.append(cat)

    return json.dumps(categories)


@app.route("/api/products/category/<cat_name>")
def get_by_category(cat_name):
    results=[]
    for prod in mock_catalog:
        if prod["category"].lower() == cat_name.lower():
            results.append(prod)
    return json.dumps(results)



@app.route("/api/products/search/<text>")
def search_by_text(text):
    results = []

    for prod in mock_catalog:
        title = prod["title"].lower()
        if text in title:
            results.append(prod)

    return json.dumps(results)

# start the server
app.run(debug=True)


""

