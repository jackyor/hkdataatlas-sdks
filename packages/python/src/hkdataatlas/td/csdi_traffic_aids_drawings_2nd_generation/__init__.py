"""A client library for accessing Transport Department — Traffic Aids Drawings (2nd generation)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
