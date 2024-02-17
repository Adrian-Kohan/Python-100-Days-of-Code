from bs4 import BeautifulSoup
import requests


response = requests.get("https://www.goodreads.com/list/show/153860.Goodreads_Top_100_Highest_Rated_Books_on_Goodreads_with_at_least_10_000_Ratings")
data = response.text
soup = BeautifulSoup(data, "html.parser")

books = []

book_name = soup.find_all(name="a", class_="bookTitle")
book_author = soup.find_all(name="a", class_="authorName")
book_rating = soup.find_all(name="span", class_="minirating")


for i in range(0, 100):
    book = {
    "Name": book_name[i].getText().split("\n")[1],
    "Author": book_author[i].getText(),
    "Ratings": book_rating[i].getText(),
    }
    books.append(book)

with open("books.csv", "a", encoding="utf-8") as file:
    file.write('        Goodreads Top 100 - Highest Rated Books on Goodreads with at least 10,000 Ratings\n\n'
               '                      Name                        ,'
               'Author                  ,Ratings          \n')

for book in books:
    with open("books.csv", "a", encoding="utf-8") as file:
        file.write(f'{book["Name"]}     , {book["Author"]}      , {book["Ratings"]}\n')
