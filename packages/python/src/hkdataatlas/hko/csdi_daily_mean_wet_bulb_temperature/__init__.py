"""A client library for accessing Hong Kong Observatory — Daily mean wet bulb temperature"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
