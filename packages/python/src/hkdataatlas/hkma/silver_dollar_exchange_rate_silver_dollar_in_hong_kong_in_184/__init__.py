"""A client library for accessing HKIMR - Silver Dollar Exchange Rate"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
