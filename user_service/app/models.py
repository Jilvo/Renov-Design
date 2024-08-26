from piccolo.table import Table
from piccolo.columns import Varchar, Email, Serial


class UserAccount(Table):
    id = Serial(primary_key=True)
    username = Varchar(max_length=100, unique=True)
    email = Email()
    password = Varchar(max_length=100)


class EmailRequest(Table):
    receiver_email: str
    subject: str
    body: str
