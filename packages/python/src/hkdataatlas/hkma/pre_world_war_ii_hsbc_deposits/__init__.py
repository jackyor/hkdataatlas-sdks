"""A client library for accessing HKIMR - Pre-World-War-II HSBC Deposits"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
