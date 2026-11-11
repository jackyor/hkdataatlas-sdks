"""A client library for accessing Security Bureau — Customised yearly statistical tables of the Central Registry of Drug Abuse (CRDA)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
