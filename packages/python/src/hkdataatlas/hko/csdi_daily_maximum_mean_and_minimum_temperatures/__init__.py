"""A client library for accessing Hong Kong Observatory — Daily maximum, mean and minimum temperatures"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
