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

# Function to get Instagram post details using Instaloader
def get_instagram_details(url):
    INSTA_LOADER = instaloader.Instaloader()
    shortcode = url.split("/")[-2] # Second last element of the url
    post = instaloader.Post.from_shortcode(INSTA_LOADER.context, shortcode)

    post_details = {
        'caption' : post.caption,
        'user_name' : post.owner_username,
        'post_date' : post.date_utc
    }
    return post_details


# Set the path to the ChromeDriver
driver_path = '/opt/homebrew/bin/chromedriver'
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Navigate to Instagram's login page
driver.get('https://www.instagram.com/accounts/login/')
time.sleep(2)

# Find the username and password input fields and send the login credentials
username_input = driver.find_element(By.NAME, 'username')
password_input = driver.find_element(By.NAME, 'password')

username_input.send_keys(INSTAGRAM_USERNAME)  
time.sleep(4)
password_input.send_keys(INSTAGRAM_PASSWORD)
time.sleep(4)
password_input.send_keys(Keys.RETURN) # Enter
time.sleep(5)

# Keyword
keyword = '나이키'
search_url = f'https://www.instagram.com/explore/tags/{keyword}/'

driver.get(search_url)
time.sleep(10)

# Extract all post links from the page using XPath
post_links = driver.find_elements(By.XPATH, '//a[contains(@href, "/p/")]')
for link in post_links:
    url = link.get_attribute('href')
    print(f"Post URL: {url}")

    post_details = get_instagram_details(url)
    print(f"Caption: {post_details['caption']}")
    print(f"User Name: {post_details['user_name']}")
    print(f"Post Date: {post_details['post_date']}")

driver.quit()
