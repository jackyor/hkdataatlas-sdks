"""A client library for accessing Education Bureau — Programme Information"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
