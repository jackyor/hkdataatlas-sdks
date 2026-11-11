"""A client library for accessing HKSTPC Tender Notice API"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
