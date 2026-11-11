"""A client library for accessing Lands Department — Short Term Tenancy"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
