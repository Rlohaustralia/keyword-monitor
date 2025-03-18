import schedule
import time
import subprocess
import os
import sys
sys.path.append(os.path.abspath('/Users/ej/keyword_monitor'))
from scraper.views import *

def scrape_data_automatically():
    try:
        os.chdir('/Users/ej/keyword_monitor')
        command = "python -m scraper.api.main keyword_text"
        os.system(command)
        time.sleep(2)
        print("🟢 WEB_SCRAPING_SCHEDULER : Data scraped sucessfully")
    except subprocess.CalledProcessError as e:
        print(f"❌ WEB_SCRAPING_SCHEDULER : Error during scraping -> {e}")

schedule.every(1).minute.do(scrape_data_automatically)

while True:
    schedule.run_pending()
    time.sleep(1)

