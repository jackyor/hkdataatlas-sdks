"""A client library for accessing Information Services Department — Office Addresses and Open Hours"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
