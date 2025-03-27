## Keyword Monitoring Web App
This project automates web scraping for user-defined keywords, stores the data in MongoDB, and provides an API for retrieval.
</br>
</br>
</br>


## Demo 🕹️
- **Main Page**
<img width="500" alt="Screenshot 2025-03-27 at 9 48 00 pm" src="https://github.com/user-attachments/assets/ed3ab7d1-799c-4622-a6b4-f0585899a67e" />
<img width="500" alt="Screenshot 2025-03-27 at 10 44 03 pm" src="https://github.com/user-attachments/assets/9d044c72-bcf4-45cb-9e5f-b4a537efb72a" />
<img width="500" alt="Screenshot 2025-03-27 at 10 11 01 pm" src="https://github.com/user-attachments/assets/d0f1ecc3-f423-40fd-9a74-703889f82efe" />
<img width="500" alt="Screenshot 2025-03-27 at 9 49 51 pm" src="https://github.com/user-attachments/assets/54143bdc-97db-4f00-a34b-f5fdbd19d0fa" />
</br>
- **Keyword CRUD (Create, Read, Update, Delete)**
<img width="1000" alt="Screenshot 2025-03-27 at 10 20 44 pm" src="https://github.com/user-attachments/assets/89f025aa-f55d-4a7c-8223-820f540ca394" />
</br>
- **Scraping (Live Monitor)**
<img width="1000" alt="Screenshot 2025-03-27 at 10 20 22 pm" src="https://github.com/user-attachments/assets/2cd5e7b5-7a57-4fde-8cd0-0f5c336b7575" />
</br>
- **Sign Up / Login / Logout**
</br>
</br>
</br>


## Features ✅
- **Automated Web Scraping** - Collects web data based on keywords  
- **MongoDB Storage** - Stores extracted data for analysis  
- **API Integration** - Provides RESTful APIs to retrieve data
- **User Authentication** - Supports user registration & sign-in
- **(Upcoming) Dashboard** - Visualizes keyword trends (🚧 Work In Process)  
</br>
</br>
</br>


## Built with
- Backend : Python, Django </br>
- Frontend : HTML, CSS, TailwindCSS </br>
- Database : MongoDB </br>
- Scraping : BeautifulSoup
</br>
</br>
</br>


## API Specification 📒
You can find the full API specification [Here!](https://ringed-mist-28d.notion.site/API-Specification-1c05a604dab480fe93e8fa75b37847e7)</br></br></br>
<img width="920" alt="Screenshot 2025-03-25 at 3 11 46 pm" src="https://github.com/user-attachments/assets/a3b1b984-39a0-42ef-ae49-7087e9d7780e" />
</br>
</br>
</br>


## MongoDB Design
The project uses MongoDB to store data. Below are the collections and their fields:</br></br>

**'keyword' collection** </br>
▸ Stores keywords for each user. </br></br>
<img width="1106" alt="Screenshot 2025-03-25 at 4 06 58 pm" src="https://github.com/user-attachments/assets/48023e96-ac06-44da-b1f4-8b9ee0f025e0" /></br>
  - `_id`: ObjectId
  - `user` : Unique identifier of the user
  - `keyword`: The keyword user added
</br>


**'scraper' collection** </br>
▸ Stores feedback collected from various social media platforms. </br></br>
<img width="1110" alt="Screenshot 2025-03-25 at 4 04 25 pm" src="https://github.com/user-attachments/assets/e938b317-6dbf-445d-ba20-51ec1c201f04" /></br>
  - `_id`: ObjectId
  - `user` : Unique identifier of the user
  - `keyword`: The keyword user added
  - `platform`: The social media platform (e.g., YouTube, Google, Naver)
  - `title`: The title of the scraped data
  - `content`: The content of the scraped data
  - `source_url`: The URL of the source where the data was found
  - `postdate`: The time when the data was posted
</br>
</br>
</br>


## How To Run
```bash
git clone https://github.com/Rlohaustralia/keyword-monitor.git
```
```bash
cd your-repo
```
```bash
pip install -r requirements.txt
```
```bash
python manage.py runserver
```
</br>
</br>
</br>



## Future Improvement 
- Develop a dashboard (including keyword trend analysis & sentiment analysis) </br>
- Set a deletion cycle for MongoDB data </br>
- Add a scheduling feature (automate periodic crawling) </br>
- Use logging to record errors while displaying general error messages to users </br>
- Prevent API daily usage limit from being exceeded (implement notifications) </br>
- Convert to JSON format (currently using form submission with application/x-www-form-urlencoded) </br>
- Improve the web UI (build a user-friendly interface) </br>

