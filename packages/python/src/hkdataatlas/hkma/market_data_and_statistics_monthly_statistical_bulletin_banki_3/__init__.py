"""A client library for accessing Customer deposits by type - Hong Kong dollar and foreign currency deposits"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
