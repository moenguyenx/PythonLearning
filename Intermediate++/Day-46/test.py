import requests
from bs4 import BeautifulSoup

# set the URL to scrape
url = 'https://www.billboard.com/charts/hot-100/2003-08-19/'

# make a request to the website
response = requests.get(url)

# create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# find the chart elements containing the song names
chart = soup.find_all('li', {'class': 'chart-list__element display--flex'})

# loop through each chart element and get the song name
for song in chart:
    title = song.find('span', {'class': 'chart-list__title'}).text
    artist = song.find('span', {'class': 'chart-list__artist'}).text
    print(title, '-', artist)