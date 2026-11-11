"""A client library for accessing Hong Kong Observatory — Daily mean amount of cloud"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
