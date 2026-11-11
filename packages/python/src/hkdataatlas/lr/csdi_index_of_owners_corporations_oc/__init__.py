"""A client library for accessing Land Registry — Index of Owners' Corporations (OC)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
