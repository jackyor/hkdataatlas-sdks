"""A client library for accessing Money supply - Adjusted for foreign currency swap deposits"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
