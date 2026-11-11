"""A client library for accessing HKSTPC Events happening in Hong Kong Science Park API"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
