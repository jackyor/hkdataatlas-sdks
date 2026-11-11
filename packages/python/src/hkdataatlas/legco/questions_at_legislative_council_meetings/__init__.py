"""A client library for accessing Questions at Legislative Council meetings"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
