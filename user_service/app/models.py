from piccolo.table import Table
from piccolo.columns import Varchar, Email


class UserAccount(Table):
    username = Varchar(max_length=100, unique=True)
    email = Email()
    password = Varchar(max_length=100)


class DatabaseError(Exception):
    def __init__(self, message="A database error occurred"):
        self.message = message
        super().__init__(self.message)
