from pymongo import MongoClient
import hashlib
import os
import json

db = MongoClient("mongodb://localhost:27017/ScreenAi")

def registro(user):
    ret=True
    try:

        posts = db.usuarios

        print(posts)

        inserted = posts.insert_one(user).inserted_id

        if(inserted == 'null'):
            ret = False
    except:
        print("Something went wrong")
        ret = False
    finally:
        return ret

def login(user):
    ret=True
    try:
        posts = db.usuarios

        inserted = posts.find_one(user)

        if(inserted == 'null'):
            ret = False
    except:
        print("Something went wrong")
        ret = False
    finally:
        return ret