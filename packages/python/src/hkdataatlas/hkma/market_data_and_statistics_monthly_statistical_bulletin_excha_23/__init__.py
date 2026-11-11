"""A client library for accessing Hong Kong dollar forward exchange rates - End of period figures"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
