"""A client library for accessing HKSTPC Restaurant List API"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
