"""A client library for accessing Legislative Council Webcast System"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
