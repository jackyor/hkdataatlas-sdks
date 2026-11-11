"""A client library for accessing Registration and Electoral Office — 2021 Voter Registration Statistics"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
