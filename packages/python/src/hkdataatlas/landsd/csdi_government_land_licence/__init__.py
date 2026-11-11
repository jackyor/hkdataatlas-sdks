"""A client library for accessing Lands Department — Government Land Licence"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
