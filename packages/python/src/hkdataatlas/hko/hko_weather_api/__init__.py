"""A client library for accessing Hong Kong Observatory Open Data API"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
