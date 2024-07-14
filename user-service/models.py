from piccolo.table import Table
from piccolo.columns import Varchar, Email


class UserAccount(Table):
    username = Varchar(length=100, unique=True)
    email = Email()
    password = Varchar(length=100)
