"""A client library for accessing Immigration Department — Immigration Branch Offices"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
