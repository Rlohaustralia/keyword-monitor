from scraper.api.search_google import search_all_keywords as search_google
from scraper.api.search_youtube import search_all_keywords as search_youtube
from scraper.api.search_naver_blog import search_all_keywords as search_naver_blog
from scraper.api.search_naver_cafe import search_all_keywords as search_naver_cafe
import sys

# Run all scrapers for keyword processing
if __name__ == "__main__":
    user = sys.argv[1]

    try:
        google_search_results = search_google(user)
        print("✅ Google Search Results:", google_search_results)
    except Exception as e:
        print("❌ Error with Google search:", e)

    try:
        youtube_search_results = search_youtube()
        print("✅ YouTube Search Results:", youtube_search_results)
    except Exception as e:
        print("❌ Error with YouTube search:", e)

    try:
        naver_blog_search_results = search_naver_blog()
        print("✅ Naver Blog Search Results:", naver_blog_search_results)
    except Exception as e:
        print("❌ Error with Naver Blog search:", e)

    try:
        naver_cafe_search_results = search_naver_cafe()
        print("✅ Naver Cafe Search Results:", naver_cafe_search_results)
    except Exception as e:
        print("❌ Error with Naver Cafe search:", e)
