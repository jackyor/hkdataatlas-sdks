"""A client library for accessing Department of Justice - Press Releases"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
