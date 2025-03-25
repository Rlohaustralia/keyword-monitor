## Keyword Monitoring Web App
This project automates web scraping for user-defined keywords, stores the data in MongoDB, and provides an API for retrieval.
</br>
</br>
</br>


## Demo 🕹️
Coming Soon...
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


## API Specification
You can find the full API specification </br>
[📒 Eng](https://ringed-mist-28d.notion.site/API-Specification-1c05a604dab480fe93e8fa75b37847e7). </br>
[📒 Kor](https://ringed-mist-28d.notion.site/API-Specification-1c05a604dab480fe93e8fa75b37847e7). </br>
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

