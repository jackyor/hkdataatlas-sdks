"""A client library for accessing Hong Kong Interbank Interest Rates - End of period figures"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
