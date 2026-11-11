"""A client library for accessing Security Bureau — Survey of Drug Use among Students"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
