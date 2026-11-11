"""A client library for accessing Lands Department — Digital Topographic Map iB10000"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
