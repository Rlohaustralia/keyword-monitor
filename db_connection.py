import pymongo

# MongoDB Connection
url = "mongodb://localhost:27017"
client = pymongo.MongoClient(url)
db = client["keyword_monitor"]