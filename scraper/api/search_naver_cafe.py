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
def get_all_keywords(user):
    keywords = keyword_collection.find({"user" : user}, {"_id" : 0, "keyword" : 1}) # Extract only keyword value
    return [item["keyword"] for item in keywords] # Convert to list


# Call Naver API
def search_naver_cafe(keyword):
    url = "https://openapi.naver.com/v1/search/cafearticle.json"
    params = {
        "query" : keyword,
        "display" : 10,
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
        print(f"Response Text: {response.text}")
        return None


# Execute searching
def search_all_keywords(user):
    keywords = get_all_keywords(user)
    print(f"🐞 Keyword found: {keywords}")

    if not keywords:
        print("🐞 There is no saved keyword")
        return
    
    results = {}

    for keyword in keywords:
        search_result = search_naver_cafe(keyword)
        if search_result:
            results[keyword] = search_result["items"]
            
            # Save data
            for item in search_result["items"]:
                print(item)
                save_scrap_data(user,
                                keyword,
                                "Naver Cafe",
                                item["title"],
                                item["description"],
                                item["link"],
                                None) # Published date is not available

    return results
