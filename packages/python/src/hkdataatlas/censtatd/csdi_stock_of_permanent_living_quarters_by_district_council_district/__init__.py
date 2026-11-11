"""A client library for accessing Census and Statistics Department — Stock of permanent living quarters by District Council district"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
