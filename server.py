

from unittest import mock
from colorama import Cursor
from flask import Flask, request, abort
import json
from mock_data import mock_catalog
from config import db
from bson import ObjectId

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
    for prod in cursor:
        total += prod["price"]

    return json.dumps(total)



#find a product based on the unique id
@app.route("/api/products/<id>")
def find_product(id):
    prod = db.products.find_one({"_id": ObjectId(id)})
    prod["_id"] = str(prod["_id"])

    return json.dumps(prod)


@app.route("/api/products/category/<cat_name>")
def get_by_category(cat_name):
    results = []
    cursor = db.products.find({"category": cat_name})
        
    for prod in cursor:
        prod["_id"] = str(prod["_id"])
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


@app.get("/api/couponCodes")
def get_coupon_codes():
    cursor = db.couponCodes.find({})
    results = []
    for coupon in cursor:
        coupon["_id"] = str(coupon["_id"])
        results.append(coupon)

    return json.dumps(results)

@app.get("/api/couponCodes/<code>")
def get_by_codes(code):
    coupon = db.couponCodes.find_one({"code":code})
    if not coupon:
        return abort(401, "not valid code")


    coupon["_id"] = str(coupon["_id"])
    return json.dumps(coupon)


@app.post("/api/couponCodes")
def save_coupon():
    coupon = request.get_json()

    #validate
    if not "code" in coupon or len(coupon["code"])< 5:
        return abort(400, "Code is req and should be atleast 5 characters")

    if not "discount" in coupon or type(coupon["discount"]) != type(int) or type(coupon["discount"]) != type(float):
        return abort(400, "Discount is required | no decimals!")    


    if coupon["discount"] < 0 or coupon["discount"] > 25:
        return abort(400, "Discount is required and should between 0 and 25%")




    db.couponCodes.insert_one(coupon)
    coupon["_id"] = str(coupon["_id"])
    
    return json.dumps(coupon)



app.run(debug=True)




