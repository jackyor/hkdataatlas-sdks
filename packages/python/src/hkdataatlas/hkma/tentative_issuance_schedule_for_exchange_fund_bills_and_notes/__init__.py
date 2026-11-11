"""A client library for accessing Tentative issuance schedule for Exchange Fund Bills and Notes"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
