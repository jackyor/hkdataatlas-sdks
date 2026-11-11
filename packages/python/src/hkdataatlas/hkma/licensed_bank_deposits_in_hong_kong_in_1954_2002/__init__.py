"""A client library for accessing HKIMR - Licensed Bank Deposits in Hong Kong"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
