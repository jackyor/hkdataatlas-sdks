"""A client library for accessing Hong Kong Interbank Interest Rates - Period average figures"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
