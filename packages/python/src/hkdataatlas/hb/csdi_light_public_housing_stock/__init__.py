"""A client library for accessing Housing Bureau — Light Public Housing Stock"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
