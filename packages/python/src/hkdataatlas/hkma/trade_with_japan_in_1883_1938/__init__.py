"""A client library for accessing HKIMR - Trade with Japan"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
