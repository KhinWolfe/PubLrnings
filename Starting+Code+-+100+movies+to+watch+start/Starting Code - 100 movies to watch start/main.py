import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
response.encoding = "utf-8"
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")
movie_titles = []

movies = soup.find_all(name="h3", class_="title")
for movie in movies:
    m_title = movie.getText()
    movie_titles.append(m_title)

movie_titles.reverse()
with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")