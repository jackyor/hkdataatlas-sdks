"""A client library for accessing Lands Department — Digital Terrain Model (DTM)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
