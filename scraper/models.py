from db_connection import db
from bs4 import BeautifulSoup
from datetime import datetime

scrap_collection = db['scrapper']

def save_scrap_data(keyword, platform, title, content, source_url, postdate):
    try:
        doc = {
            "keyword": keyword,
            "platform": platform,
            "title": remove_html_tags(title),
            "content": remove_html_tags(content),
            "source_url": source_url,
            "postdate": postdate.strftime("%Y-%m-%dT%H:%M:%SZ")
        }
        # Use update_one to update existing documents or insert new ones
        result = scrap_collection.update_one(
            {"source_url": source_url},  # Check if this URL already exists
            {"$set": doc},               # Update all fields
            upsert=True                   # Insert if not exists
        )

        if result.upserted_id:
            return {"success": True, "message": "New document inserted."}
        elif result.modified_count > 0:
            return {"success": True, "message": "Existing document updated."}
        else:
            return {"success": False, "message": "No changes were made (data might be the same)."}
    except Exception as e:
        return {"success": False, "message": str(e)}
        
# Remove HTML tags
def remove_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()
