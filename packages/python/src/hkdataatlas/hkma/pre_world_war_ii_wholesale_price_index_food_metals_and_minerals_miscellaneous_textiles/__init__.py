"""A client library for accessing HKIMR - Pre-World-War-II Wholesale Price Index"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
