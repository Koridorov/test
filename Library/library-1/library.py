from book import Book
import json
from member import (Member, PremiumMember, StudentMember)

from member import (BorrowLimitError,BookNotAvialableError, BookNotBorrowedError)

class Library():
    def __init__(self, name):
        self.name=name
        self.books=dict()
        self.members=dict()

    def add_book(self, book:Book):
        if book.isbn in self.books.keys():
            raise ValueError
        self.books[book.isbn]=book

    def remove_book(self, isbn):
        if isbn not in self.books.keys():
            raise ValueError("This book is not present in the library. Please enter another ISBN. ")
        self.books.pop(isbn)

    def register_member(self, member:Member):
        self.members[member.member_id]=member

    def find_by_author(self, author:str):
        book_list=[]
        for _ in self.books.values():
            if _.author.lower()==author.lower():
                book_list.append(_)
        return book_list
    
    def find_by_title(self, title:str):
        book_list_title=[]
        for _ in self.books.values():
            if (str(title)).lower() in str(_.title).lower():
                book_list_title.append(_)
        return book_list_title

    def lend(self, isbn, member_id):
        member=self.members.get(member_id)
        book=self.books.get(isbn)
        try:
            member.borrow_book(book)
        except BorrowLimitError:
            print(f"{member.name} has reached the limit of {member.MAX_BOOKS} books.")
        except BookNotAvialableError:
            print(f'"{book.title}" is currently borrowed by someone else.')
        else:
            print(f'{member.name} borrowed "{book.title}".')

    def return_books(self, isbn, member_id):
            member=self.members.get(member_id)
            book=self.books.get(isbn)
            member.return_book(book)
            
    def get_available_books(self):
        book_list_available=[]
        for _ in self.books.values():
            if _.is_available:
                book_list_available.append(_)
        return book_list_available

    def report(self):
        print(f"""
This Library manages {len(self.books)} books.
The available books are: {self.get_available_books()}.
This Library manages {len(self.members)} members.
            """)
        print("Borrowed Books:", end=" ")
        for member in self.members.values():
            if member.borrowed_books:
                print(f"{member.name}: {member.borrowed_books}", end=";")

    def load_library(self):
        f=open("C:\\Users\\User\\Desktop\\Coding\\Library\\library-1\\mydata.json", "r")
        [books_raw, members_raw]=json.load(f)
        self.books={key:Book.from_dict(book) for key, book in books_raw.items()}
        self.members={key:Member.from_dict(member) for key, member in members_raw.items()}
        f.close()

    def save_library(self):
        f=open("C:\\Users\\User\\Desktop\\Coding\\Library\\library-1\\mydata.json", "w")
        plain_books={key: book.to_dict() for key, book in self.books.items()}
        plain_members={key: member.to_dict() for key, member in self.members.items()}
        json.dump(([plain_books, plain_members]), f)
        f.close()