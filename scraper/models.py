from django.db import models
from db_connection import db
from pymongo import MongoClient, ASCENDING
from datetime import datetime
import os

# Create your models here.
scrap_collection = db['Scrapper']

# 컬렉션 인덱스 설정 (중복 방지)
scrap_collection.create_index([("source_url", ASCENDING)], unique=True)

def save_comment(keyword, platform, title, content, source_url):
    try:
        doc = {
            "keyword" : keyword,
            "platform" : platform,
            "title" : title,
            "content" : content,
            "source_url" : source_url,
            "timestamp" : datetime.utcnow()
        }
        scrap_collection.insert_one(doc)
        return True
    except:
        return False