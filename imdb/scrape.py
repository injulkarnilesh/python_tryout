import requests
from bs4 import BeautifulSoup
import csv

series = 'tt0108778'
season = 1
url = 'https://www.imdb.com/title/{}/episodes'.format(series);
params = dict(season=season)
episodespage = requests.get(url, params)

soup = BeautifulSoup(episodespage.content, 'html.parser')

title = soup.find('div', class_='subpage_title_block__right-column')
titlename = title.find('a').text

seasonselector = soup.find('select', id = 'bySeason')
seasonoptions = seasonselector.find_all('option')
totalseasons = len(seasonoptions)

with open(titlename + '.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['title', 'season', 'episodenumber', 'episodename', 'rating'])

while season <= totalseasons:
    url = 'https://www.imdb.com/title/{}/episodes'.format(series)
    params = dict(season=season)
    episodespage = requests.get(url, params)

    soup = BeautifulSoup(episodespage.content, 'html.parser')
    episodes = soup.find_all('div', class_ = 'list_item')

    ratings = []
    episodenumber = 1
    for episode in episodes:
        rating = episode.find('span', class_='ipl-rating-star__rating')
        name = episode.find('strong')
        ratings.append((titlename, season, episodenumber, name.text, float(rating.text)))
        episodenumber += 1

    with open(titlename + '.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(ratings)

    season += 1
