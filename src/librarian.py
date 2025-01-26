from user import User


class Librarian(User):
    def __init__(self, employee_id):
        super().__init__()
        self.__employee_id = employee_id

    def can_borrow(self, book):
        return not book.get_is_borrowed()
