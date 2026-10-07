from book import Book

class BookNotAvialableError(Exception):
        pass
class BorrowLimitError(Exception):
        pass
class BookNotBorrowedError(Exception):
        pass
    

class Member():

    MAX_BOOKS=3
    count=0

    def __init__(self, name:str):
        self.name=name
        Member.count+=1
        self.member_id=str(Member.count)
        self.borrowed_books=[]

    def borrow_book(self, book:Book):
        """If available and not at MAX_BOOKS marks the book as unavailable and appends it to borrowed_books list. """
        if len(self.borrowed_books)>=self.MAX_BOOKS:
            raise BorrowLimitError("The book is not available to borrow or you have reached the borrow limit. ")
        elif book.is_available==False:
            raise BookNotAvialableError("The book is not available to borrow. ")
        else:
            self.borrowed_books.append(book)
            book.borrow()

    def return_book(self, book:Book):
        """If book is in borrowed_books removes it and calls book.give_back()"""
        if book not in self.borrowed_books:
            raise BookNotBorrowedError("You have not borrowed this book. Please enter a borrowed book. ")
        else:
            self.borrowed_books.remove(book)
            book.give_back()

    def __str__(self):
        return f"{self.name}, ID Number {self.member_id}. Currently borrowing {len(self.borrowed_books)} books."

class StudentMember(Member):

    MAX_BOOKS=5

    def __init__(self, name, university):
        super().__init__(name)
        self.university=university

    def __str__(self):
        return f"Student member {self.name} from {self.university}, ID Number {self.member_id}. Currently borrowing {len(self.borrowed_books)} books."

class PremiumMember(Member):

    MAX_BOOKS=10

    def __init__(self, name, membership_fee):
        super().__init__(name)
        self.membership_fee=membership_fee
     
    def reserve_book(self, book:Book):
        print("WIP")

    def __str__(self):
        return f"Premium member {self.name}, ID Number {self.member_id}. Currently borrowing {len(self.borrowed_books)} books. Your membership fee is {self.membership_fee}."