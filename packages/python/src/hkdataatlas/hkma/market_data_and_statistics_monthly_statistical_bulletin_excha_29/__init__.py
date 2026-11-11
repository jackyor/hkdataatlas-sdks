"""A client library for accessing Hong Kong dollar interest rates - Rates as at effective dates"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
