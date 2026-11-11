"""A client library for accessing HKSTPC Company Directory API"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
