
from flask import Flask, request


app = Flask(__name__) 


stores = [
    {
        "name": "Ella Dress",
        "items": [
            {
                "title" : "Robe",
                "price" : 15.89
            },
            {
                "title" : "Modash",
                "price" : 20.00
            }
        ]
    },
    {
        "name" : "Marel Fish",
        "items" : [
            {
                "name" : "Siliure",
                "price" : 25.14
            },
            {
                "name" : "Carpe",
                "price" : 16.48

            }
        ]
    }
]

@app.get("/stores")

def all_stores():

    return stores


@app.post("/stores")

def create_store():

    request_data = request.get_json()
    
    new_store = {"name" : request_data["name"], "item" : []}

    stores.append(new_store)

    return stores , 201 

""" @app.post("/stores/<string:name>/item")
def create_item(name):

    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name" : request_data["name"], "price" : request_data["price"]}

            store["items"].append(new_item)

            return new_item , 201
    return '{"Message":"Store not found"}', 404 """

@app.post("/stores/<string:name>/item")
def create_item(name):
    request_data = request.get_json()

    for store in stores:
        if store["name"] == name:
            # Ensure 'items' key exists and is a list
            if "items" not in store:
                store["items"] = []

            # Create the new item with standardized 'name' and 'price' keys
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)

            return new_item, 201

    return {"Message": "Store not found"}, 404
