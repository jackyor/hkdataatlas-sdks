"""A client library for accessing Hong Kong Observatory — Wet Bulb Globe Temperature"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
