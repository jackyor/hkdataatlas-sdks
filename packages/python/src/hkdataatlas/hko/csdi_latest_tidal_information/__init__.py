"""A client library for accessing Hong Kong Observatory — Latest tidal information"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
