# coding: utf-8
import pymongo
from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.myDB
db.myCol.insert_one({
        "Persons": [{"id": "201511082", "이름": "김가령"},
                    {"id": "201511082", "이름": "가령"}]
    })
results = db.myCol.find()
for r in results:
    print r['Persons']