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


def normalize_date_published(date_published):
    # "2024-12-24T01:13:57Z" -> YYYYMMDD
    if date_published:
        normalize_date_published = date_published[:4] + date_published[5:7] + date_published[8:10]
        return normalize_date_published
    
# Execute searching
def search_all_keywords():
    keywords = get_all_keywords()
    print(f"🐞 Keyword found: {keywords}")

    if not keywords:
        print("🐞 There is no saved keyword")
        return
    
    results = {}

    for keyword in keywords:
        search_result = search_youtube(keyword)
        if search_result:
            results[keyword] = search_result["items"]

            for video in search_result["items"]:  
                video_id = video["id"].get("videoId")  # "videoId"를 가져옴
                if not video_id:
                    continue  # videoId가 없으면 건너뜀

                video_url = f"https://www.youtube.com/watch?v={video_id}"
                video_published_date = video["snippet"]["publishedAt"]
                normalized_published_date = normalize_date_published(video_published_date)

                save_scrap_data(keyword,
                                "YouTube",
                                video["snippet"]["title"],
                                video["snippet"]["description"],
                                video_url,
                                normalized_published_date
                )
    return results