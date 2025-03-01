import requests
import os
from dotenv import load_dotenv
from db_connection import db
import sys
from scraper.models import save_scrap_data


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


load_dotenv()

YOUTUBE_API = os.getenv("YOUTUBE_API")

keyword_collection = db['keyword']


# Extract keywords from db
def get_all_keywords():
    keywords = keyword_collection.find({}, {"_id" : 0, "keyword" : 1})
    return [item["keyword"] for item in keywords]


# Call YouTube API
def search_youtube(keyword):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part" : "snippet",
        "q" : keyword,
        "type" : "video", 
        "maxResults" : 5,
        "key" : YOUTUBE_API
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"❌ API request failed (Keyword): {keyword}) - Status Code: {response.status_code}")
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
        search_result = search_youtube(keyword)
        if search_result:
            results[keyword] = search_result["videos"]

            for video in search_result["videos"]:
                video_url = "https://www.youtube.com/watch?v=" + video["id"] 
                save_scrap_data(keyword,
                                "YouTube",
                                video["snippet"]["title"],
                                video["snippet"]["description"],
                                video_url,
                                video["snippet"]["publishedAt"])
    return results

if __name__ == "__main__":
    search_results = searach_all_keywords()
    
                
