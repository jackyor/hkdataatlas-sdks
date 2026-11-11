"""A client library for accessing Education Bureau — School Registration Information"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
