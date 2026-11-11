"""A client library for accessing HKIMR - Land Revenues of the HK Government in 1844-1940"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
