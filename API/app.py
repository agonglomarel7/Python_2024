
from flask import Flask 


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