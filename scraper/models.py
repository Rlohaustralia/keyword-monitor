from db_connection import db
from bs4 import BeautifulSoup

# Create your models here.
scrap_collection = db['scrapper']

def save_scrap_data(keyword, platform, title, content, source_url, postdate):
    try:
        doc = {
            "keyword": keyword,
            "platform": platform,
            "title": remove_html_tags(title),
            "content": remove_html_tags(content),
            "source_url": source_url,
            "postdate": postdate
        }
        # Use update_one with upsert=True to ignore duplicates
        result = scrap_collection.update_one(
            {"source_url": source_url},  # Filter for existing document
            {"$setOnInsert": doc},       # Insert if it doesn't exist
            upsert=True                   # Create if it doesn't exist (Update + Insert)
        )
        return result.upserted_id is not None  # Returns True if a new document was created
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


# Remove html tags
def remove_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

