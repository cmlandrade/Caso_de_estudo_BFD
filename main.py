from datetime import datetime
from abc import ABC, abstractmethod
from book_database import books_db
from member_database import members_db


book = []
member = []
loan = []

def save_book_db(book_data):
    books_db.append(book_data)

def register_new_book():
    
    max_id = 0
    for livro in books_db:
        current_id = livro["idBook"]
        if current_id > max_id:
            max_id = current_id
    new_id = max_id + 1
    title = input("Insert title: ")
    author = input("Insert Author: ")
    genre = input("Insert genre: ")
    publish_date = input("Insert publish date (AAAA-MM-DD): ")

    new_book = Book(
        idBook=new_id, 
        title=title, 
        author=author, 
        genre=genre, 
        publish_date=publish_date
    )

    new_book.registerBook()
    
    print(f"Book '{title}'(ID: {new_id}) registered.")

class Book:
    def __init__(self, idBook, title, author, genre, publish_date):
        self.idBook = idBook
        self.title = title
        self.author = author
        self.genre = genre
        self.publish_date = publish_date

    def to_dict(self):
        return {
            "idBook": self.idBook,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "publish_date": self.publish_date
        }

    def registerBook(self):

        book_data = self.to_dict()
        save_book_db(book_data)

