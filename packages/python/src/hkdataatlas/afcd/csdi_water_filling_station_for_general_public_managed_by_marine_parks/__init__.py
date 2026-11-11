"""A client library for accessing Agriculture, Fisheries and Conservation Department — Water Filling Station for General Public Managed by Marine Parks"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
