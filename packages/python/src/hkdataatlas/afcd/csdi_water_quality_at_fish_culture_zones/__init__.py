"""A client library for accessing Agriculture, Fisheries and Conservation Department — Water Quality at Fish Culture Zones"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
