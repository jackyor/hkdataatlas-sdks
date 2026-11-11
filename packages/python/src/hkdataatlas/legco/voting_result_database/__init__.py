"""A client library for accessing Legislative Council Voting Result Database"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
