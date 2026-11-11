"""A client library for accessing Hong Kong and Kowloon Ferry Limited Open Data API"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
