"""A client library for accessing Legislative Council Bills Database"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
