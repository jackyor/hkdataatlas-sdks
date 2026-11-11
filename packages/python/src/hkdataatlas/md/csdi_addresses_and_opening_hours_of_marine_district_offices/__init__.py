"""A client library for accessing Marine Department — Addresses and Opening Hours of Marine District Offices"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
