"""A client library for accessing Marine Department — Areas where Bright Light Fishing is Permitted"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
