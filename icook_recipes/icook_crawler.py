import requests
from bs4 import BeautifulSoup

from pathlib import Path
import os
import shutil

HTML_PARSER = 'html.parser'
ICOOK_URL = 'https://icook.tw/recipes/latest'

def get_icook_latest_recipes():
    res = requests.get(ICOOK_URL)
    if res.status_code == requests.codes.ok:
        soup = BeautifulSoup(res.content, HTML_PARSER)
        recipes = soup.find_all('div', class_='latest-browse-recipe')

        for recipe in recipes:
            id = recipe['data-recipe-id']
            cover = recipe.find('div', class_='browse-recipe-cover')
            imgsrc = cover.find('img')['data-src']
            content = recipe.find('div', class_='browse-recipe-content')
            title = content.find('a', class_='browse-recipe-name')['data-title']

            recipedir = Path('recipes').joinpath('{}-{}'.format(id, title))
            if not recipedir.exists():
            	os.makedirs(str(recipedir))
            	imgres = requests.get(imgsrc, stream=True)
            	if imgres.status_code == requests.codes.ok:
            		with open(str(recipedir.joinpath('img.jpg')), 'wb') as output:
            			shutil.copyfileobj(imgres.raw, output)


if __name__ == '__main__':
    get_icook_latest_recipes()
