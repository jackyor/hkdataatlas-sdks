"""A client library for accessing Hong Kong Monetary Authority — Register of AIs and LROs"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
