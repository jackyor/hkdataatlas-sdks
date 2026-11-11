"""A client library for accessing Hong Kong Observatory — Daily grass minimum temperature"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
