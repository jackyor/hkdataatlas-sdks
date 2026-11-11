"""A client library for accessing Loans and advances by type - Authorized institutions"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
