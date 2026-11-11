"""A client library for accessing HKIMR - Trade with the United Kingdom"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
