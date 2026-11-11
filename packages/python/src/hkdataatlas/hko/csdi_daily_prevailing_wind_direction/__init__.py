"""A client library for accessing Hong Kong Observatory — Daily prevailing wind direction"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
