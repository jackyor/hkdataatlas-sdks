"""A client library for accessing Registration and Electoral Office — Election Results of 2016 Legislative Council General Election"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
