from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import instaloader

load_dotenv()
INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

def get_instagram_details(url):
    INSTA_LOADER = instaloader.Instaloader()
    shortcode = url.split("/")[-2]  # Extract the shortcode from the URL
    post = instaloader.Post.from_shortcode(INSTA_LOADER.context, shortcode)

    post_details = {
        'caption' : post.caption,
        'user_name' : post.owner_username,
        'post_date' : post.date_utc
    }
    return post_details


# ChromeDriver
driver_path = '/opt/homebrew/bin/chromedriver'
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Login (Instagram)
driver.get('https://www.instagram.com/accounts/login/')
time.sleep(2)

username_input = driver.find_element(By.NAME, 'username')
password_input = driver.find_element(By.NAME, 'password')

username_input.send_keys(INSTAGRAM_USERNAME)  
time.sleep(2)
password_input.send_keys(INSTAGRAM_PASSWORD)
time.sleep(2)
password_input.send_keys(Keys.RETURN)  # Enter
time.sleep(5)

# Keyword
keyword = '미즈노'
search_url = f'https://www.instagram.com/explore/tags/{keyword}/'

driver.get(search_url)
time.sleep(5)

# Scroll down to load more posts
scroll_limit = 3  # Scroll down 3 times
for _ in range(scroll_limit):
    driver.execute_script("window.scrollBy(0, 1000);") # Execute JavaScript code / scrolls 1000 pixels downward
    time.sleep(3)  # Wait for new posts to load

# Extract links
post_links = driver.find_elements(By.XPATH, '//a[contains(@href, "/p/")]')

# Set a limit for the number of posts to scrape
max_posts = 10
count = 0

for link in post_links:
    if count >= max_posts:  # Stop after scraping max posts
        break
    
    url = link.get_attribute('href')
    print(f"Post URL: {url}")

    post_details = get_instagram_details(url)
    print(f"Caption: {post_details['caption']}")
    print(f"User Name: {post_details['user_name']}")
    print(f"Post Date: {post_details['post_date']}")
    
    count += 1

driver.quit()
