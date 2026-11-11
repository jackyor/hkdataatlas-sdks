"""A client library for accessing Hong Kong Observatory — Hourly ambient gamma radiation level in Hong Kong"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
