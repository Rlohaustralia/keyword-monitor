from scraper.api.search_google import search_all_keywords as search_google
from scraper.api.search_youtube import search_all_keywords as search_youtube
from scraper.api.search_naver_blog import search_all_keywords as search_naver_blog
from scraper.api.search_naver_cafe import search_all_keywords as search_naver_cafe


# Run all scrapers for keyword processing
if __name__ == "__main__":
    google_search_results = search_google()
    print(google_search_results)

    youtube_search_results = search_youtube()
    print(youtube_search_results)

    naver_blog_search_results = search_naver_blog()
    print(naver_blog_search_results)

    naver_cafe_search_results = search_naver_cafe()
    print(naver_cafe_search_results)
