"""A client library for accessing Registration and Electoral Office — Election Results of 2019 District Council Ordinary Election"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
