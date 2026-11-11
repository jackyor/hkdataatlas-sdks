"""A client library for accessing Education Bureau — School Location and Information"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
