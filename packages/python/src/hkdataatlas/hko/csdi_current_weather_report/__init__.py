"""A client library for accessing Hong Kong Observatory — Current weather report"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
