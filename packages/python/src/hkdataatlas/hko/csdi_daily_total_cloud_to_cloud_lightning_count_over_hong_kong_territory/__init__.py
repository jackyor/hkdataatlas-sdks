"""A client library for accessing Hong Kong Observatory — Daily total cloud-to-cloud lightning count over Hong Kong territory"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
