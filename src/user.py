class User:
    def __init__(self, first_name, surname, email):
        self.__first_name = first_name
        self.__surname = surname
        self.__email_address = email
        self.__borrowed_books = []

    def get_first_name(self):
        return self.__first_name

    def get_surname(self):
        return self.__surname

    def get_email_address(self):
        return self.__email_address

    def get_borrowed_books(self):
        return self.__borrowed_books

    def can_borrow_book(self, book):
        return len(self.__borrowed_books) < 5 and not book.is_borrowed()

    def borrow_book(self, book):
        if self.can_borrow_book(self):
            self.__borrowed_books.append(book)
            book.set_is_borrowed(True)

    def return_book(self, book):
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)
            book.set_is_borrowed(False)
