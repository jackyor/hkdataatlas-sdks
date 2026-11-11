"""A client library for accessing Hong Kong Observatory — Regional weather in Hong Kong – the latest 10-minute mean visibility"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
