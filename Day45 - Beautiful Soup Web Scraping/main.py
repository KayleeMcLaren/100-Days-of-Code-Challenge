
from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
empire_webpage = response.text
soup = BeautifulSoup(empire_webpage, "html.parser")

titles_list = soup.find_all(name="h3", class_="title")

movies_titles = [movie.getText() for movie in titles_list]
movies = movies_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
        
