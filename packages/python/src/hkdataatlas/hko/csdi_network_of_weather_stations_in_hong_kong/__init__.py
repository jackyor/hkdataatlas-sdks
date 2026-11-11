"""A client library for accessing Hong Kong Observatory — Network of Weather Stations in Hong Kong"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
