from django.db import models
from db_connection import db

# Create your models here.
keyword_collection = db['keyword']

# Create
def add_keyword(keyword_text):
    keyword_collection.insert_one({"keyword" : keyword_text})

# Read
def get_all_keywords():
    keywords = [doc.get("keyword", "") for doc in keyword_collection.find()]
    return keywords

# Update
def update_keyword(old_keyword, new_keyword):
    keyword_collection.update_one({"keyword" : old_keyword}, {"$set" : {"keyword" : new_keyword}})

# Delete
def delete_keyword(keyword_text):
    keyword_collection.delete_one({"keyword" : keyword_text})