"""A client library for accessing Hong Kong dollar interbank transactions"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
