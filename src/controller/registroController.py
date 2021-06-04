from pymongo import MongoClient
import hashlib
import os
import json

client = MongoClient("mongodb://localhost:27017")
db = client.ScrenAi

def registro(user):
    ret=True
    try:
        salt = os.urandom(32)

        posts = db.usuarios

        inserted = posts.insert_one(user).inserted_id

        if(inserted == 'null'):
            ret = False
    except:
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
        ret = False
    finally:
        return ret