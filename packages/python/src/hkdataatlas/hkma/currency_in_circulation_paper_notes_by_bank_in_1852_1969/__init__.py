"""A client library for accessing HKIMR - Currency in Circulation: Paper Notes by Bank"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
