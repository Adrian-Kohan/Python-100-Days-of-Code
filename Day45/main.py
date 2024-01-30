from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
movies = response.text
soup = BeautifulSoup(movies, "html.parser")
list_of_100_movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")

main_list = [movie.getText() for movie in list_of_100_movies]

for i in range(99, -1, -1):
    with open("movies.txt", "a") as file:
        file.write(f"{main_list[i]}\n")



# with open("website.html", encoding="utf8") as file:
#     data = file.read()
#
# soup = BeautifulSoup(data, "html.parser")
# print(soup.title)