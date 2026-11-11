"""A client library for accessing Hong Kong Observatory — Daily total rainfall"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
