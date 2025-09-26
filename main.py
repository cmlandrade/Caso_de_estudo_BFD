from datetime import datetime
from abc import ABC, abstractmethod
from book_database import books_db
from member_database import members_db


book = []
member = []
loan = []

def save_book_db(book_data):
    books_db.append(book_data)


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
    
    @classmethod
    def registerBook(cls):
    
        ini_id = 0
        for livro in books_db:
            current_id = livro["idBook"]
            if current_id > ini_id:
                ini_id = current_id
        new_id = ini_id + 1
        title = input("Insert title: ")
        author = input("Insert Author: ")
        genre = input("Insert genre: ")
        publish_date = input("Insert publish date (AAAA-MM-DD): ")

        print(f"Book '{title}'(ID: {new_id}) registered.")

        new_book = cls(
            idBook=new_id, 
            title=title, 
            author=author, 
            genre=genre, 
            publish_date=publish_date
            )
        save_book_db(new_book.to_dict())




Book.registerBook()

class Member:
    def __init__(self, cpf, name, email, password):
        self.idMember = cpf
        self.name = name
        self.email = email
        self.password = password
    
    def register_Member(self):
        members[self.idMember] = self
        print(f"\n Parabéns,{self.name}. Sua conta foi cadastrada com sucesso!")
    
    '''def listLoan(self):'''

    def search_Member(self, idMember):
        return members.get(idMember)
    
    '''def listMembers(self):'''

    def delete_Member(self):
        if self.idMember in members:
            del members[self.idMember]
            print(f"Até mais,{self.name}. Sua conta foi deletada com sucesso! ")
        else:
            print("Não foi possível encontrar sua conta.")

class Loan:
    def __init__ (self, member, book, dateOrder, dateReturn):
        self.idLoan = len(loan) + 1
        self.member = member
        self.book = book
        self.dateOrder = dateOrder
        self.dateReturn = dateReturn

    def create_Loan(self, member, book):
        return Loan(member, book)
    
    def cancel_Loan(self):
      self.status = "Cancelado"
      print(f"Empréstimo {self.idLoan} cancelado com sucesso!")

    def confirm_Loan(self):
        self.status = "Confirmado"
        print(f"Empréstimo {self.idLoan} confirmado com sucesso!")

    '''def get_details(self)'''
