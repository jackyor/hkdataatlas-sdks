"""A client library for accessing Hong Kong Housing Authority — Location and Profile of Public Housing Estates"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
