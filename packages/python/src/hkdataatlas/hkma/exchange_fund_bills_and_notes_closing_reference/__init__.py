"""A client library for accessing Exchange Fund Bills and Notes Closing Reference-Bills"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
