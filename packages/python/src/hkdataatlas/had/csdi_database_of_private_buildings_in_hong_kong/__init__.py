"""A client library for accessing Home Affairs Department — Database of private buildings in Hong Kong"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
