"""A client library for accessing Marine Department — Private Mooring Areas"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
