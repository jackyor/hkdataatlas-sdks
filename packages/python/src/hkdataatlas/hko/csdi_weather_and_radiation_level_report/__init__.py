"""A client library for accessing Hong Kong Observatory — Weather and radiation level report"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
