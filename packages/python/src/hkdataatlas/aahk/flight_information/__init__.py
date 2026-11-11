"""A client library for accessing Hong Kong International Airport Flight Information"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
