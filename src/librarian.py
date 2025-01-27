from user import User


class Librarian(User):
    def __init__(self, first_name, surname, email, employee_id):
        super().__init__(first_name, surname, email)
        self.__employee_id = employee_id

    def can_borrow(self, book):
        """Method overriding example"""
        return not book.get_is_borrowed()

    def get_first_name(self, *args):
        """Method overloading example"""
        string = super().get_first_name()
        for arg in args:
            string += arg
        return string

    def get_email_address(self, hide):
        """Method overloading example"""
        return "*"
