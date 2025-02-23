from pymongo import MongoClient

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017")
db = client["keyword_monitor"]
keyword_collection = db["Keyword"]