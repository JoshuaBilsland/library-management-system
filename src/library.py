class Library:
    def __init__(self):
        self.__books = []
        self.__users = []
        self.__staff = []

    def get_books(self):
        return self.__books

    def get_users(self):
        return self.__users

    def get_staff(self):
        return self.__staff

    def add_book(self, book):
        self.__books.append(book)

    def add_user(self, user):
        self.__users.append(user)

    def add_staff(self, staff):
        self.__staff.append(staff)
