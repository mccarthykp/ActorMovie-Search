import requests
from pprint import pprint
from bs4 import BeautifulSoup
from fastapi import FastAPI

app = FastAPI()

# get actor filmography
@app.get('/get_filmography/{actor_name}')
async def get_filmography(actor_name: str):
  query = actor_name.replace(' ', '_')
  
  session = requests.Session()
  base_url = 'https://www.rottentomatoes.com'
  url = f'{base_url}/celebrity/{query}'
  
  headers = {'Accept-Language': 'en-US, en;q=0.5'}
  
  response = session.get(url, headers=headers)
  
  actor_soup = BeautifulSoup(response.text, 'html.parser')
  
  movie_names = []
  
  a_tags = actor_soup.select('table tr td a')
  
  for index, tag in enumerate(a_tags):
    text = tag.get_text()
    movie_names.extend(text)
    
  return {'Filmography': movie_names}

# get movie cast
@app.get('/get_movie_cast/{movie_name}')
async def get_movie_cast(movie_name: str):
  query = movie_name.replace(' ', '_')

  session = requests.Session()
  base_url = 'https://www.rottentomatoes.com'
  url = f'{base_url}/m/{query}'
    
  headers = {'Accept-Language': 'en-US, en;q=0.5'}
    
  response = session.get(url, headers=headers)

  movie_soup = BeautifulSoup(response.text, 'html.parser')

  cast_names = []

  all_cast_members = movie_soup.find_all('div', class_='cast-and-crew-item')
    
  for index, actor_names in enumerate(all_cast_members):
    name_elements = actor_names.find('div', class_='metadata')
    cast_names.extend(name_elements.a.p)
  
  return {'Movie Cast': cast_names}

# get movie cast
@app.get('/get_tv_cast/{show_name}')
async def get_tv_cast(show_name: str):
  query = show_name.replace(' ', '_')

  session = requests.Session()
  base_url = 'https://www.rottentomatoes.com'
  url = f'{base_url}/tv/{query}'
    
  headers = {'Accept-Language': 'en-US, en;q=0.5'}
    
  response = session.get(url, headers=headers)

  tv_soup = BeautifulSoup(response.text, 'html.parser')

  cast_names = []

  all_cast_members = tv_soup.find_all('div', class_='cast-and-crew-item')
    
  for index, actor_names in enumerate(all_cast_members):
    name_elements = actor_names.find('div', class_='metadata')
    cast_names.extend(name_elements.a.p)
  
  return {'TV Cast': cast_names}
