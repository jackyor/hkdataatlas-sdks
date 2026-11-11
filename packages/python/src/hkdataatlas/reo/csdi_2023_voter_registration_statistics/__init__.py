"""A client library for accessing Registration and Electoral Office — 2023 Voter Registration Statistics"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
