from member import (Member, BorrowLimitError, BookNotBorrowedError, BookNotAvialableError)
from book import Book
from library import Library

Biblioteka=Library("Biblioteka")

class Menu():

    def main(self):
        print(f"1. Add a book \n2. Register a member \n3. Lend a book \n4. Return a book \n5. Search books \n6. Show report\n0. Exit\nEnter your choice:")
    
    def continue_button(self):
        while True:
            print()
            print (f"0. Return to menu.")
            try:
                value=int(input())
            except ValueError:
                print("Please enter a number. ")
                continue
            match value:
                case 0:
                    break
                case _:
                    print("Maika ti da eba!!!!")

    def search_books(self):
        while True:
            print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n1. Search by author\n2. Search by title\n0. Exit\nEnter your choice:")
            try:
                value=int(input())
            except ValueError:
                print("Please enter a number. ")
                continue
            match value:
                    case 1:
                        author=input("Enter the first and last name of the author: ")
                        print(Biblioteka.find_by_author(author))
                        self.continue_button()
                    case 2:
                        title=input("Enter any part of the title you are looking for: ")
                        print(Biblioteka.find_by_title(title))
                        self.continue_button()
                    case 0:
                        print("bybye nigga")
                        break
                    case _:
                        print("Maika ti da eba!!!!!!!!!")

    def run(self):
        while True:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n ")
            self.main()
            try:
                value=int(input())
            except ValueError:
                print("Please enter a number. ")
                continue
            match value:
                    case 1:
                        title=input("Enter the book's title: ")
                        author=input("Enter the book's author: ")
                        isbn=input("Enter the book's ISBN: ")
                        year=input("Enter the book's release year: ")
                        try:
                            book=Book(title, author, isbn, year)
                            try:
                                Biblioteka.add_book(book)
                                print(f"{book.title} has been added to the library database.")
                                self.continue_button()
                            except ValueError:
                                print("This book with this ISBN is already present in the library. Please enter another ISBN. ")
                                self.continue_button()
                        except ValueError:
                            print("Please enter a year between 1000 and 2026")
                            self.continue_button()

                    case 2:
                        name=input("Enter your name: ")
                        member=Member(name)
                        Biblioteka.register_member(member)
                        print(f"Member {name} has been registered. Your member ID is {member.member_id}.")
                        self.continue_button()

                    case 3:
                        member_id=input("Enter your member ID: ")
                        isbn=input("Enter the ISBN of the book you'd like to lend: ")

                        book=Biblioteka.books.get(isbn)
                        member=Biblioteka.members.get(member_id)

                        try:
                            Biblioteka.lend(isbn, member_id)
                            print(f"The book {book.title} has been successfully lent to {member.name}.")
                            self.continue_button()
                        except ValueError:
                            print("The ISBN or the member ID is invalid. Please try again.")
                            self.continue_button()
                        except BorrowLimitError:
                            print("This member has already reached their borrow limit.")
                            self.continue_button()
                        except BookNotAvialableError:
                            print(f"{book} is not available. Please try a different book.")
                        except AttributeError:
                            self.continue_button()

                    case 4:
                        member_id=input("Enter your member ID: ")
                        isbn=input("Enter the ISBN of the book you'd like to return: ")

                        book=Biblioteka.books.get(isbn)
                        member=Biblioteka.members.get(member_id)
                        try:
                            Biblioteka.return_books(isbn, member_id)
                            print(f"The book {book.title} has been successfully returned to the library by {member.name}.")
                            self.continue_button()
                        except ValueError, AttributeError:
                            print("The ISBN or the member ID is invalid. Please try again.")
                            self.continue_button()
                        except BookNotBorrowedError:
                            print(f"The book with this ISBN is not borrowed by {member.name}")
                            self.continue_button()
                        
                    case 5:
                        self.search_books()
                    case 6: 
                        print("----------report----------")
                        Biblioteka.report()
                        self.continue_button()

                    case 0:
                        print("Byeee")
                        break
                    case _:
                        print("maika ti da eba")
if __name__=="__main__":
    menu=Menu()
    menu.run()
