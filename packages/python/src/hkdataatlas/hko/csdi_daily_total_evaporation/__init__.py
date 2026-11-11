"""A client library for accessing Hong Kong Observatory — Daily total evaporation"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
