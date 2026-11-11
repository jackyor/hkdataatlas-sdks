"""A client library for accessing Analysis of NCDs issued in Hong Kong"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
