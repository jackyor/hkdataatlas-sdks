"""A client library for accessing Hong Kong Housing Authority — Housing Construction Programme (HCP) under Hong Kong Housing Authority"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
