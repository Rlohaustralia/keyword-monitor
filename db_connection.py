import pymongo
import os
from dotenv import load_dotenv

# MongoDB Connection
MONGO_URL = os.getenv("MONGO_URL")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB_NAME]