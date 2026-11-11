"""A client library for accessing Hong Kong Observatory — Lightning count over Hong Kong territory in the past hour"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
