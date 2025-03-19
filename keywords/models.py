from django.db import models
from db_connection import db

# Create your models here.
keyword_collection = db['keyword']
scrap_collection = db['scrapper']

# Create
def add_keyword(user, keyword_text):
    keyword_collection.insert_one({"user": user, "keyword" : keyword_text})

# Read
def get_all_keywords(user):
    keywords = [doc.get("keyword", "") for doc in keyword_collection.find({"user" : user})]
    return keywords

# Update
def update_keyword(user, old_keyword, new_keyword):
    keyword_collection.update_one({"user": user, "keyword" : old_keyword}, {"$set" : {"keyword" : new_keyword}})

# Delete
def delete_keyword(user, keyword_text):
    keyword_collection.delete_one({"user": user, "keyword" : keyword_text})