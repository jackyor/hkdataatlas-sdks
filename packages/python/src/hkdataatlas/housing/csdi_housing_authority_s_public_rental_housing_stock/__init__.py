"""A client library for accessing Hong Kong Housing Authority — Housing Authority's Public Rental Housing Stock"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
