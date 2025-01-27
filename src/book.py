class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
        self.__is_borrowed = False

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_is_borrowed(self):
        return self.__is_borrowed

    def set_is_borrowed(self, boolean):
        self.__is_borrowed = boolean
