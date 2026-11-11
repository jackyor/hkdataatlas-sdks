"""A client library for accessing Hong Kong Observatory — Daily mean dew point temperature"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
