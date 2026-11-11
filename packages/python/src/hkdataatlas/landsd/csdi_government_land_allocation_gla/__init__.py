"""A client library for accessing Lands Department — Government Land Allocation (GLA)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
