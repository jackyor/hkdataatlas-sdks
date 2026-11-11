"""A client library for accessing Marine Department — Height restriction areas in Hong Kong waters"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
