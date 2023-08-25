# TomatoGrove
A Rotten Tomatoes web scraper using BeautifulSoup4, written in Python. 
## How to Run
1. Download Repo `git clone`
2. Enter project folder
3. Create a new virtual environment `python -m venv venv`
4. Activate the venv `source venv/bin/activate`
4. Install dependencies `pip install -r requirements.txt`
5. Run with `uvicorn app:app --reload`

## How to Use
Endpoints are used with custom queries to serve scraped data.

1. <strong>/get_filmography/{actor_name}</strong> <br>
Retrieves all cast appearances by the queried actor.

2. <strong>/get_movie_cast/{movie_name}</strong> <br>
Retrieves all cast members featured in the queried movie.

3. <strong>/get_tv_cast/{show_name}</strong> <br>
Retrieves all cast members featured in the queried television show.
