"""A client library for accessing Hong Kong Observatory — Daily mean wind speed"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
