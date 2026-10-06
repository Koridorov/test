from book import Book

from member import (Member, PremiumMember, StudentMember)

from member import (BorrowLimitError,BookNotAvialableError, BookNotBorrowedError)

class Library():
    def __init__(self, name):
        self.name=name
        self.books=dict()
        self.members=dict()

    def add_book(self, book:Book):
        if book.isbn in self.books.keys():
            raise ValueError("This book is already present in the library. Please enter another ISBN. ")
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
        member=Member(self.members.get(member_id))
        book=(self.books.get(isbn))
        try:
            member.borrow_book(book)
        except (BorrowLimitError, BookNotAvialableError):
            print("The book is not available to borrow or you have reached the borrow limit. ")
        except (AttributeError, KeyError):
            print("Either the ISBN or the member ID is invalid. Please check both. ")


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
        print("Borrowed Books:")
        for member in self.members.values():
            if member.borrowed_books:
                print(f" - {member.name}: {member.borrowed_books}")