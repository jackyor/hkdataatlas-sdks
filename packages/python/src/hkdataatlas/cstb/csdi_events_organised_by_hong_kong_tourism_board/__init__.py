"""A client library for accessing Culture, Sports and Tourism Bureau — Events organised by Hong Kong Tourism Board"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
