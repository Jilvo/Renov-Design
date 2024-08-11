"""import model de base pydantic"""

from pydantic import BaseModel


class APIErrorMessage(BaseModel):
    type: str
    message: str


class DomainError(Exception):
    message: str


class DataValidationError(Exception):
    message: str


class ResourceNotFound(DomainError):
    pass


class QueryError(DomainError):
    pass


class RepositoryError(DomainError):
    @classmethod
    def save_operation_failed(cls) -> "RepositoryError":
        return cls("An error occurred during saving to the database!")

    @classmethod
    def get_operation_failed(cls) -> "RepositoryError":
        return cls("An error occurred while retrieving the data from the database!")
