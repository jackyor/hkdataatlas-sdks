"""A client library for accessing Hong Kong Observatory — Daily maximum and mean Hong Kong Heat Index"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
