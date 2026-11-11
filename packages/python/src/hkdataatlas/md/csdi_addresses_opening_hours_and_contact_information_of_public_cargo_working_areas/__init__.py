"""A client library for accessing Marine Department — Addresses, Opening Hours and Contact Information of Public Cargo Working Areas"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
