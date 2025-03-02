import requests
import os
from dotenv import load_dotenv
from db_connection import db
import sys
from scraper.models import save_scrap_data


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


load_dotenv()

NAVER_CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
NAVER_CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")

keyword_collection = db['keyword']

# Extract keywords from db
def get_all_keywords():
    keywords = keyword_collection.find({}, {"_id" : 0, "keyword" : 1}) # Extract only keyword value
    return [item["keyword"] for item in keywords] # Convert to list


# Call Naver API
def search_naver_blog(keyword):
    url = "https://openapi.naver.com/v1/search/blog.json"
    params = {
        "query" : keyword,
        "display" : 5,
        "start" : 1,
        "sort" : "sim"
    }

    headers = {
        "X-Naver-Client-Id": NAVER_CLIENT_ID,
        "X-Naver-Client-Secret": NAVER_CLIENT_SECRET
    }
   
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        print(f"🐞 JSON: {response.json()}")
        return response.json()
    else:
        print(f"❌ API request failed (Keyword): {keyword}) - Status Code: {response.status_code}")
        return None


# Execute searching
def search_all_keywords():
    keywords = get_all_keywords()
    print(f"🐞 Keyword found: {keywords}")

    if not keywords:
        print("🐞 There is no saved keyword")
        return
    
    results = {}

    for keyword in keywords:
        search_result = search_naver_blog(keyword)
        if search_result:
            results[keyword] = search_result["items"]
            
            # Save data
            for item in search_result["items"]:
                save_scrap_data(keyword,
                                "Naver Blog",
                                item["title"],
                                item["description"],
                                item["link"],
                                item["postdate"])

    return results


if __name__ == "__main__":
    search_results = search_all_keywords()
    print(search_results)

