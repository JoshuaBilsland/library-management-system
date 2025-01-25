class Library:
    def __init__(self):
        self.__books = []
        self.__members = []
        self.__staff = []

    def get_books(self):
        return self.__books

    def get_members(self):
        return self.__members

    def get_staff(self):
        return self.__staff

    def add_book(self, book):
        self.__books.append(book)

    def add_member(self, member):
        self.__members.append(member)

    def add_staff(self, staff):
        self.__staff.append(staff)
