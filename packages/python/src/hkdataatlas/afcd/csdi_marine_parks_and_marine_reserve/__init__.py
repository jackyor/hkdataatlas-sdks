"""A client library for accessing Agriculture, Fisheries and Conservation Department — Marine Parks and Marine Reserve"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
