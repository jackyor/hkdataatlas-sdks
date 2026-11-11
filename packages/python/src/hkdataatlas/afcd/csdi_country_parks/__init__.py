"""A client library for accessing Agriculture, Fisheries and Conservation Department — Country Parks"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
