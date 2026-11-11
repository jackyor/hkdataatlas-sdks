"""A client library for accessing Agriculture, Fisheries and Conservation Department — Government Wholesale Food Markets"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
