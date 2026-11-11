"""A client library for accessing Immigration Department — Marriage Registries"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
