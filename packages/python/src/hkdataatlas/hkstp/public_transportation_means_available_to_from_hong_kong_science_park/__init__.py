"""A client library for accessing HKSTPC Available Public Transportation API"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
