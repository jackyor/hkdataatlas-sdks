"""A client library for accessing Census and Statistics Department — Stock of permanent living quarters by area and type"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
