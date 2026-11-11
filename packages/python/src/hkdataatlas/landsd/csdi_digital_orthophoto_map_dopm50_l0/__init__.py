"""A client library for accessing Lands Department — Digital Orthophoto Map DOPM50-L0"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
