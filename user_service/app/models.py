from piccolo.table import Table
from piccolo.columns import Varchar, Email, Serial, Text, Date


class UserAccount(Table):
    id = Serial(primary_key=True)
    username = Varchar(max_length=100, unique=True)
    email = Email()
    password = Varchar(max_length=100)
    date_of_birth = Date()


class EmailRequest(Table):
    id = Serial(primary_key=True)
    receiver_email = Email()
    subject = Varchar(max_length=255)
    body = Text()
