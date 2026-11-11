"""A client library for accessing Lands Department — Digital Orthophoto DOP5000"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
