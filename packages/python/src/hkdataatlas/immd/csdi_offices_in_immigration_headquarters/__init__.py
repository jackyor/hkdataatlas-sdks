"""A client library for accessing Immigration Department — Offices in Immigration Headquarters"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
