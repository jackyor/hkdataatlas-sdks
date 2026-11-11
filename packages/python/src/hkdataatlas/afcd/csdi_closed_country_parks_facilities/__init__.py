"""A client library for accessing Agriculture, Fisheries and Conservation Department — Closed country parks facilities"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
