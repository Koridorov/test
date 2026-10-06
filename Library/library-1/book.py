class Book():
    total_books=0

    def __init__(self, title:str, author:str, isbn:str, year:str):
        if not self.is_valid_isbn(isbn):
            raise ValueError("The ISBN is not correct. Please enter a correct ISBN.")


        self.title=title
        self.author=author
        self.isbn=isbn
        self.year=year
        self.__is_available=True
        Book.total_books+=1

    @property
    def is_available(self):
           return self.__is_available

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if 1000<=int(year)<=2026:
            self._year=year
        else:
            raise ValueError("Please enter a year between 1000 and 2026. ")

    def borrow(self:Book) -> bool:
        """If the book is available, makes it unavailable and returns True. Otherwise returns False. """
        if self.__is_available==True:
            self.__is_available=False
            return True
        return False

    def give_back(self:Book) -> bool:
        """Makes the book available again and returns True if the book is unavailable. Otherwise returns False. """
        if self.__is_available==False:
            self.__is_available=True
            return True
        return False

    def __str__(self):
        return f"\"{self.title}\" by {self.author} ({self.year}) - {"Available" if self.__is_available==True else "Unavailable"}"

    def __repr__(self):
        #return f"Book(title=={self.title}, author=={self.author}, isbn=={self.isbn}, year=={self.year})"
        return f"\"{self.title}\" by {self.author} ({self.year})" #{"Available" if self.__is_available==True else "Unavailable"}"

    @staticmethod
    def is_valid_isbn(isbn:str):
        if (len(isbn.replace("-",""))==10 or len(isbn.replace("-",""))==13) and isbn.replace("-","").isdigit():
            return True
        return False
    
    #this is a staticmethod because this does not "touch" the class, instead only looks at it. from_string MAKES a new instance of class, so it is a class method

    @classmethod
    def from_string(cls, text:str) -> Book:
        return cls(text.split(";")[0], text.split(";")[1], text.split(";")[2], text.split(";")[3])
        #cls(*text.split(";"))
        #or list parts= text.split(";") and then parts [1,2,3,4...]

    @classmethod
    def get_total_books(cls):
        return cls.total_books