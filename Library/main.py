from member import (Member, BorrowLimitError, BookNotBorrowedError, BookNotAvialableError)
from book import Book
from library import Library

Biblioteka=Library("Biblioteka")

class Menu():

    def main(self):
        print(f"1. Add a book \n2. Register a member \n3. Lend a book \n4. Return a book \n5. Search books \n6. Show report\n0. Exit")

    def search_books(self):
        print(f"1. Search by author\n2. Search by title\n0. Exit \nEnter your choice:")

    def run(self):
        while True:
            print(" ")
            self.main()
            try:
                value=int(input())
                match value:
                    case 1:
                        print("Add a book")
                        title=input("Enter the book's title: ")
                        author=input("Enter the book's author: ")
                        isbn=input("Enter the book's ISBN: ")
                        year=input("Enter the book's release year: ")

                        book=Book(title, author, isbn, year)
                        Biblioteka.add_book(book)

                    case 2:
                        print("Register a member")

                        name=input("Enter your name: ")
                        Biblioteka.register_member(Member(name))

                    case 3:
                        print("Lend a book")

                        member_id=input("Enter your member ID: ")
                        isbn=input("Enter the ISBN of the book you'd like to lend: ")

                        Biblioteka.lend(isbn, int(member_id))


                    case 4:
                        print("Return a book")

                        member_id=input("Enter your member ID: ")
                        isbn=input("Enter the ISBN of the book you'd like to return: ")
                        Biblioteka.return_books(isbn, int(member_id))
                        
                    case 5:
                        print("Search books")
                        while True:
                            print(" ")
                            self.search_books()
                            value=int(input())
                            match value:
                                    case 1:
                                        author=input("Enter the first and last name of the author: ")
                                        print(Biblioteka.find_by_author(author))
                                    case 2:
                                        title=input("Enter any part of the title you are looking for: ")
                                        print(Biblioteka.find_by_title(title))
                                    case 0:
                                        print("bybye nigga")
                                        break
                    case 6: 
                        print("Show report")

                        Biblioteka.report()

                    case 0:
                        print("Exit")
                        break
                    case _:
                        print("maika ti da eba")

            except ValueError:
                print("Please enter a number: ")
                continue
if __name__=="__main__":
    menu=Menu()
    menu.run()
