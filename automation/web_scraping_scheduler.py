import schedule
import time
import subprocess
import os
import sys


def scrape_data_automatically():
    try:
        command = "python -m scraper.api.main keyword_text"
        os.system(command)
        time.sleep(2)
        print("🟢 WEB_SCRAPING_SCHEDULER : Data scraped sucessfully")
    except subprocess.CalledProcessError as e:
        print(f"❌ WEB_SCRAPING_SCHEDULER : Error during scraping -> {e}")

schedule.every(1).minute.do(scrape_data_automatically)

while True:
    schedule.run_pending()
    time.sleep(2)

