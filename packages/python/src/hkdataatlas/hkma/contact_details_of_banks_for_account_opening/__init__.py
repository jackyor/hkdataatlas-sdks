"""A client library for accessing Contact details of banks for account opening"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
