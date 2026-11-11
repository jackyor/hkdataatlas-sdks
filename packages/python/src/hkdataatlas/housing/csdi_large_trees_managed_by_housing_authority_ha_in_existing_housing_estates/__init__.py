"""A client library for accessing Hong Kong Housing Authority — Large Trees managed by Housing Authority (HA) in existing housing estates"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
