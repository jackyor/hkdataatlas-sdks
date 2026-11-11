"""A client library for accessing HKIMR - Currency In Circulation: Paper Notes, Coins, and Total"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
