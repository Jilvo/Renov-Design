from piccolo.table import Table
from piccolo.columns import Varchar, Email


class UserAccount(Table):
    username = Varchar(max_length=100, unique=True)
    email = Email()
    password = Varchar(max_length=100)

    @staticmethod
    async def get_user_by_email(email):
        return (
            await UserAccount.select().where(UserAccount.email == email).first().run()
        )


class DatabaseError(Exception):
    def __init__(self, message="A database error occurred"):
        self.message = message
        super().__init__(self.message)
