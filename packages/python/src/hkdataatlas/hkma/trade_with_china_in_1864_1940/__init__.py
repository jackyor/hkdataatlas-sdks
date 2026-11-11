"""A client library for accessing HKIMR - Trade with China"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
