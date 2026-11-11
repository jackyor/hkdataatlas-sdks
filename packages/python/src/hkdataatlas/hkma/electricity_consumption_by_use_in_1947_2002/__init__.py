"""A client library for accessing HKIMR - Electricity Consumption by Use"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
