import requests
from pprint import pprint
from bs4 import BeautifulSoup

# Movie Search
# URL = 'https://www.imdb.com/search/title/?groups=top_100&ref_=adv_prv'
# headers = {'Accept-Language': 'en-US, en;q=0.5'}
# results = requests.get(URL, headers=headers)
# movie_soup = BeautifulSoup(results.text, 'html.parser')

# movie_names = []
# movie_div = movie_soup.find_all('div', class_='lister-item mode-advanced')

# for index, container in enumerate(movie_div):
#       name = container.h3.a.text
#       movie_names.append(f'{index+1}. {name}')

# pprint.pprint(movie_names)

# Actor Search
query = input('Actor name: ')
query = query.split(' ')
query = '_'.join(query)

session = requests.Session()
base_url = 'https://www.rottentomatoes.com'
url = f'{base_url}/celebrity/{query}'

headers = {'Accept-Language': 'en-US, en;q=0.5'}
response = session.get(url, headers=headers)

actor_soup = BeautifulSoup(response.text, 'html.parser')

movie_names = []

a_tags = actor_soup.select("table tr td a")
for index, tag in enumerate(a_tags):
    text = tag.get_text()
    print(f"{index + 1}. {text}")



# movie_div = actor_soup.find_all('div', class_='scroll-x')

# for index, container in enumerate(movie_div):
#     name = container.table.a.text
#     movie_names.append(f'{index+1}. {name}')
# pprint(movie_names)

# for movie_table in movie_div:
#     table = movie_table.find('tbody', class_='celebrity-filmography__tbody')

# for table_row in table:
#     title = table_row.find_all('td', class_='celebrity-filmography__title')
#     movie_names.append(title)
    # movie_names.append(movie_name)

# pprint(movie_names)
# actor_div = actor_soup.find_all('div', class_='lister-item-content')
# for container in actor_div:
#       actor_url = container.h3.a['href']
      
# actor_url = f'{base_url}{actor_url}'
# response = session.get('https://www.imdb.com/title/tt0322330/fullcredits')
# pprint.pprint(response)
