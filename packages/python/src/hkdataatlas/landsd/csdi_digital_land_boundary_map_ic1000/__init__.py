"""A client library for accessing Lands Department — Digital Land Boundary Map iC1000"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
