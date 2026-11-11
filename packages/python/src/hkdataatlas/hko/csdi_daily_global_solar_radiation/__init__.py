"""A client library for accessing Hong Kong Observatory — Daily global solar radiation"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
