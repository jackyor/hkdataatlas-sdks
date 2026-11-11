"""A client library for accessing Lands Department — Digital Topographic Map iB5000"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
