"""A client library for accessing Hong Kong Observatory — Daily number of hours of reduced visibility"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
