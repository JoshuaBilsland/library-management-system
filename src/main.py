from library import Library
from book import Book
from user import User
from librarian import Librarian


def main():
    # Set up the system
    my_library = Library()
    book_one = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book_two = Book("To Kill a Mockingbird", "Harper Lee")
    book_three = Book("1984", "George Orwell")
    book_four = Book("Pride and Prejudice", "Jane Austen")
    book_five = Book("The Catcher in the Rye", "J.D. Salinger")
    book_six = Book("The Hobbit", "J.R.R. Tolkien")
    my_library.add_book(book_one)
    my_library.add_book(book_two)
    my_library.add_book(book_three)
    my_library.add_book(book_four)
    my_library.add_book(book_five)
    my_library.add_book(book_six)
    user_one = User("John", "Doe", "john@email.com")
    user_two = User("Jane", "Smith", "jane@email.com")
    staff_one = Librarian("Alice", "Johnson", "alice@email.com", "123")
    my_library.add_user(user_one)
    my_library.add_user(user_two)
    my_library.add_staff(staff_one)


if __name__ == '__main__':
    main()
