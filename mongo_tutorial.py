from pymongo import *

client = MongoClient()
db = client["vfx"]

collection = db["users"]
print("collection built")
user = dict()
user["first_name"] = "Mortin"
user["last_name"] = "Staats"
user["age"] = 32

collection.insert_one(user)

print("DB SAVED")