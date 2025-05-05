import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db_connection import db
# Create your models here.

scrap_collection = db['scrapper']

def get_keyword_counts_by_user(user):
    
    docs = scrap_collection.find({"user" : user})
    keyword_counts = {}

    for doc in docs:
        keyword = doc.get("keyword")
        if keyword not in keyword_counts:
            keyword_counts[keyword] = 1
        else:
            keyword_counts[keyword] += 1

    return keyword_counts

print(get_keyword_counts_by_user("12"))

