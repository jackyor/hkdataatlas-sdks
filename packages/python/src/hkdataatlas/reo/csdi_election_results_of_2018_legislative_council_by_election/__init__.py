"""A client library for accessing Registration and Electoral Office — Election Results of 2018 Legislative Council By-election"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
