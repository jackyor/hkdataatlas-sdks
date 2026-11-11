"""A client library for accessing HKIMR - Numbers of Licensed Banks, Bank Branches, and Bank Offices in Hong Kong"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
