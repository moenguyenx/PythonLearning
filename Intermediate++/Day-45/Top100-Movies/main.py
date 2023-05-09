import requests
from bs4 import BeautifulSoup


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")


movies_titles = [title.getText() for title in soup.find_all(name='h3', class_='title')]
movies = movies_titles[::-1]  # Reverse order of the movies list

with open("movie.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
