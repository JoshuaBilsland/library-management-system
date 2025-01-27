from library import Library
from book import Book
from user import User
from librarian import Librarian


def main():
    # Setup the system
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

    # Test accessing user vs staff information
    print(my_library.get_users()[0].get_first_name())
    print(my_library.get_staff()[0].get_first_name())

    # Test borrowing books
    # --- Test if same book can't be borrowed by multiple users
    my_library.get_users()[0].borrow_book(my_library.get_books()[0])
    my_library.get_users()[1].borrow_book(my_library.get_books()[0])
    print(my_library.get_users()[0].get_borrowed_books())
    print(my_library.get_users()[1].get_borrowed_books())

    # --- Test that user can't borrow more than 5 books
    my_library.get_users()[0].borrow_book(my_library.get_books()[1])
    my_library.get_users()[0].borrow_book(my_library.get_books()[2])
    my_library.get_users()[0].borrow_book(my_library.get_books()[3])
    my_library.get_users()[0].borrow_book(my_library.get_books()[4])
    my_library.get_users()[0].borrow_book(my_library.get_books()[5])
    print(my_library.get_users()[0].get_borrowed_books())

    # --- Test if staff can borrow more than 5 books
    my_library.get_users()[0].return_book(my_library.get_books()[0])
    my_library.get_users()[0].return_book(my_library.get_books()[1])
    my_library.get_users()[0].return_book(my_library.get_books()[2])
    my_library.get_users()[0].return_book(my_library.get_books()[3])
    my_library.get_users()[0].return_book(my_library.get_books()[4])

    my_library.get_staff()[0].borrow_book(my_library.get_books()[0])
    my_library.get_staff()[0].borrow_book(my_library.get_books()[1])
    my_library.get_staff()[0].borrow_book(my_library.get_books()[2])
    my_library.get_staff()[0].borrow_book(my_library.get_books()[3])
    my_library.get_staff()[0].borrow_book(my_library.get_books()[4])
    my_library.get_staff()[0].borrow_book(my_library.get_books()[5])
    for book in my_library.get_staff()[0].get_borrowed_books():
        print(book.get_title())

    # --- Test method overloading
    print(my_library.get_staff()[0].get_first_name("1", "2", "3"))
    print(my_library.get_staff()[0].get_email_address(True))


if __name__ == '__main__':
    main()
