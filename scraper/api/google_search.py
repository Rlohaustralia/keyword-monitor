import requests
import os
from dotenv import load_dotenv
from db_connection import db
import sys
from scraper.models import save_scrap_data


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CX = os.getenv("GOOGLE_CX")

keyword_collection = db['keyword']


# Extract keywords from db
def get_all_keywords():
    keywords = keyword_collection.find({}, {"_id" : 0, "keyword" : 1})
    return [item["keyword"] for item in keywords]


# Call Google API
def search_google(keyword):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": keyword,
        "key": GOOGLE_API_KEY,  
        "cx": GOOGLE_CX, 
        "num": 5
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"❌ API request failed (Keyword): {keyword}) - Status Code: {response.status_code}")
        print(response.text)
        
        return None

def extract_date_published(item):
    if "pagemap" in item and "metatags" in item["pagemap"]:
        for tag in item["pagemap"]["metatags"]:
            if "datePublished" in tag:
                return tag["datePublished"]
    return None
            
# Execute searching
def searach_all_keywords():
    keywords = get_all_keywords()
    print(f"🐞 Keyword found: {keywords}")

    if not keywords:
        print("🐞 There is no saved keyword")
        return
    
    results = {}

    for keyword in keywords:
        search_result = search_google(keyword)
        if search_result:
            results[keyword] = search_result["items"]

            for item in search_result["items"]:
                date_published = extract_date_published(item)
                save_scrap_data(
                keyword,
                "Google",
                item["title"],
                item["snippet"],
                item["link"],
                date_published,
                )
    return results

            
if __name__ == "__main__":
    search_results = searach_all_keywords()
    print(search_results)