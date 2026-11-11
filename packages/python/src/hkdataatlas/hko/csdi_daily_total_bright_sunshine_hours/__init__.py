"""A client library for accessing Hong Kong Observatory — Daily total bright sunshine (hours)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
