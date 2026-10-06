from book import Book
from member import Member
from library import Library

#book1=Book(1984, "George Orwell", "9780451524935", 1984)
#print(Book.get_total_books()) 
#book1=Book.from_string("1984;George Orwell;12345;1984")

#book2=Book("The Sun also Rises", "Ernest Hemingway", "9780451524935", 1967)

#book3=Book("Hamlet", "William Shakespeare", "9780451524935", 1500)

#book1.borrow()


#book1.year=1969

#print(book1.is_available)

#print(book1, book2, book3)
#print(f"{book1!r}, {book2!r}, {book3!r}")
#print(Book.get_total_books()) 

Library1=Library("Library1")
book1=Book(1984, "George Orwell", "9780451524935", 1984)
member1=Member("Stefan Stambolov")

Library1.add_book(book1)
Library1.register_member(member1)

Library1.report()
#print(Library1.find_by_title(84))
