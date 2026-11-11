"""A client library for accessing Lands Department — Land Sale Records"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
