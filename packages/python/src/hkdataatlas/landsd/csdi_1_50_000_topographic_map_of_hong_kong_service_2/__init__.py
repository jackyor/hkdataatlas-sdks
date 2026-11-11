"""A client library for accessing Lands Department — 1:50 000 Topographic Map of Hong Kong"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
