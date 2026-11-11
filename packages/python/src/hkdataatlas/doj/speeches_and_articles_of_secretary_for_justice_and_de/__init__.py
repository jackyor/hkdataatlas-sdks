"""A client library for accessing Department of Justice - Speeches and Articles"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
