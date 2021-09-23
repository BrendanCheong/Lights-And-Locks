import yaml
from pymongo import MongoClient

db = yaml.load(open('db_local.yaml'), Loader=yaml.FullLoader)
cluster = MongoClient(db["mongo_uri"])

db = cluster[db["mongo_db_name"]]
collection = db["products"]
results = collection.find({})
for doc in results:
    print(doc)
